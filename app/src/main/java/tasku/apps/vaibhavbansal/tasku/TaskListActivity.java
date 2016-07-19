package tasku.apps.vaibhavbansal.tasku;




import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v7.app.AppCompatActivity;


public class TaskListActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.generic_activity_layout_frame);



        FragmentManager fm = getSupportFragmentManager();
        //access the fragment container defined in the activity
        Fragment fragment = fm.findFragmentById(R.id.id_fragment_container);
        if(fragment == null){
            fragment = new TaskListFragment();
            fm.beginTransaction().add(R.id.id_fragment_container, fragment).commit();
        }
    }


}
