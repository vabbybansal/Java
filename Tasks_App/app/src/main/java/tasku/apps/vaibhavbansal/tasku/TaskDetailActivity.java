package tasku.apps.vaibhavbansal.tasku;



import android.content.Context;
import android.content.Intent;
import android.content.res.Resources;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v7.app.AppCompatActivity;

import java.util.UUID;

/**
 * Created by VAIBHAV on 7/19/2016.
 */
public class TaskDetailActivity extends AppCompatActivity{


    //a string constant to identify the desired task. Contains the task uuid
    private static final String EXTRA_TASK_ID = "tasku.apps.vaibhavbansal.tasku.extra_task_id";
    private static final String EXTRA_WHAT_TO_DO_WITH_INTENT = "tasku.apps.vaibhavbansal.tasku.extra_what_to_do_with_intent";



    public static Intent newIntent(Context packageContext, String whatToDO, UUID taskId){
        Intent intent = new Intent(packageContext, TaskDetailActivity.class);
        intent.putExtra(EXTRA_WHAT_TO_DO_WITH_INTENT, whatToDO);
        intent.putExtra(EXTRA_TASK_ID, taskId);
//        if(whatToDO.equals("Create New Task")){
//            //nothing to be passed in through the intent in this case
//        }

        return intent;
    }

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.generic_activity_layout_frame);

        FragmentManager fm = getSupportFragmentManager();
        Fragment fragment = fm.findFragmentById(R.id.id_fragment_container);
        if(fragment == null){
//            fragment = new TaskDetailFragment();
            fragment = createFragment();
            fm.beginTransaction().add(R.id.id_fragment_container, fragment).commit();
        }


    }
    private Fragment createFragment(){
        String whatToDoWithIntent = (String) getIntent().getSerializableExtra(EXTRA_WHAT_TO_DO_WITH_INTENT);
        UUID taskId = (UUID) getIntent().getSerializableExtra(EXTRA_TASK_ID);
        return TaskDetailFragment.newInstance(whatToDoWithIntent, taskId);
    }
}
