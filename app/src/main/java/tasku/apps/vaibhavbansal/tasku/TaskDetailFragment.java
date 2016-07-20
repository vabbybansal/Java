package tasku.apps.vaibhavbansal.tasku;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.app.ActionBarActivity;
import android.support.v7.app.AppCompatActivity;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

import java.util.Date;
import java.util.UUID;

/**
 * Created by VAIBHAV on 7/19/2016.
 */
public class TaskDetailFragment extends Fragment{

    private static final String ARG_TASK_ID = "task_id";
    private static final String ARG_WHAT_TO_DO_WITH_INTENT = "what_to_do_with_intent";


    //View Variables
    private Button createTaskButton;
    private EditText titleEditText;
    private EditText descriptionEditText;
    private Spinner prioritySpinner;
    //logic variables
    private UUID taskId;
    private Boolean isEditFrag = false;


    public static TaskDetailFragment newInstance(String whatToDoWithIntent, UUID taskId){
        //taskId is null in case of whatToDo = "Create new Task"
        Bundle args = new Bundle();
        args.putSerializable(ARG_WHAT_TO_DO_WITH_INTENT, whatToDoWithIntent);
        args.putSerializable(ARG_TASK_ID, taskId);
        TaskDetailFragment fragment = new TaskDetailFragment();
        fragment.setArguments(args);

        return fragment;

    }

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setHasOptionsMenu(true);
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {



        View view = inflater.inflate(R.layout.fragment_detailed_view, container, false);
        titleEditText = (EditText) view.findViewById(R.id.id_detail_view_task_title);
        descriptionEditText = (EditText) view.findViewById(R.id.id_detail_view_task_description);
        prioritySpinner = (Spinner) view.findViewById(R.id.id_detail_view_priority_spinner);


        String whatToDoWithIntent = (String) getArguments().getSerializable(ARG_WHAT_TO_DO_WITH_INTENT);
        taskId = (UUID) getArguments().getSerializable(ARG_TASK_ID);

        handleWhatToDoWithIntent(view, whatToDoWithIntent, taskId);

        return view;


    }
    private void handleWhatToDoWithIntent(View view, String whatToDoWithIntent, final UUID taskId){

        String toolbarTitle = new String();
        //if it's an add new task, set visible the Create New Task Button
        if(whatToDoWithIntent.equals(getString(R.string.app_constant_create_new_task))){
            toolbarTitle = getString(R.string.title_create_a_new_task);
            createTaskButton = (Button) view.findViewById(R.id.id_detail_view_create_task_button);
            createTaskButton.setVisibility(View.VISIBLE);
            createTaskButton.setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View view) {
                    Task newTask = new Task();
                    newTask.setTitle(titleEditText.getText().toString());
                    newTask.setDescription(descriptionEditText.getText().toString());
                    newTask.setPriority(prioritySpinner.getSelectedItem().toString());
                    newTask.setIs_done(false);
                    newTask.setDate_created(new Date());
                    TaskLab.get(getActivity()).addTask(newTask);
                    getActivity().finish();
                }
            });


        }
        //if it is an edit task
        else if (whatToDoWithIntent.equals(getString(R.string.app_constant_show_existing_task))){
            toolbarTitle = " " + getString(R.string.title_edit_task);
            isEditFrag = true;
            Task selectedTask = TaskLab.get(getActivity()).getTask(taskId);
            populateFields(selectedTask);
        }


        //Update ToolBar Title accordingly.
        handleAppCompatToolbar(toolbarTitle);

    }

    private void handleAppCompatToolbar(String toolbarTitle){
        // (Need to cast the activity as AppCompatActivity to get the function getSupportActionBar)
        ((AppCompatActivity)getActivity()).getSupportActionBar().setTitle(toolbarTitle);
        //set icon in case of edit
        if(isEditFrag){
            ((AppCompatActivity)getActivity()).getSupportActionBar().setDisplayShowHomeEnabled(true);
            ((AppCompatActivity)getActivity()).getSupportActionBar().setDisplayUseLogoEnabled(true);
            ((AppCompatActivity)getActivity()).getSupportActionBar().setLogo(R.drawable.ic_edit_icon);
        }

    }

    private void populateFields(Task selectedTask) {
        titleEditText.setText(selectedTask.getTitle().toString());
        descriptionEditText.setText(selectedTask.getDescription().toString());
        prioritySpinner.setSelection(getSpinnerIndex(prioritySpinner, selectedTask.getPriority()));
    }
    private int getSpinnerIndex(Spinner spinner, String myString)
    {
        int index = 0;
        for (int i=0;i<spinner.getCount();i++){
            if (spinner.getItemAtPosition(i).toString().equalsIgnoreCase(myString)){
                index = i;
                break;
            }
        }
        return index;
    }

    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        super.onCreateOptionsMenu(menu, inflater);
        if(isEditFrag){
            inflater.inflate(R.menu.fragment_task_detail, menu);
        }

    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        switch(item.getItemId()){

            case(R.id.id_menu_item_delete):
                TaskLab.get(getActivity()).deleteTask(taskId);
                getActivity().finish();
                return true;
            default:return super.onOptionsItemSelected(item);
        }


    }
}
