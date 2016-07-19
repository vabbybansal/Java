package tasku.apps.vaibhavbansal.tasku;



import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v7.app.AppCompatActivity;

/**
 * Created by VAIBHAV on 7/19/2016.
 */
public class TaskDetailActivity extends AppCompatActivity{

    public static Intent newIntentNoArgs(Context packageContext){
        Intent intent = new Intent(packageContext, TaskDetailActivity.class);
        return intent;
    }

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.generic_activity_layout_frame);

        FragmentManager fm = getSupportFragmentManager();
        Fragment fragment = fm.findFragmentById(R.id.id_fragment_container);
        if(fragment == null){
            fragment = new TaskDetailFragment();
            fm.beginTransaction().add(R.id.id_fragment_container, fragment).commit();
        }


    }
}
