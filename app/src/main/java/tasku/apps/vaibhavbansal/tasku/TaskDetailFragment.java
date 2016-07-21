package tasku.apps.vaibhavbansal.tasku;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
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
import android.widget.TextView;
import android.widget.Toast;

import java.util.Date;
import java.util.UUID;

/**
 * Created by VAIBHAV on 7/19/2016.
 */
public class TaskDetailFragment extends Fragment{

    private static final String ARG_TASK_ID = "task_id";
    private static final String ARG_WHAT_TO_DO_WITH_INTENT = "what_to_do_with_intent";

    //this is a tag for the DatePickerFragment(Dialog Fragment) and helps in its identification by the hosting activity
    private static final String DIALOG_DATE = "DialogDate";
    //constant for the TaskDetailFragment to identify that the date passed back is from the DatePickerFragment
    private static final int REQUEST_DATE  = 0;

    //View Variables
    private Button createTaskButton;
    private Button updateTaskButton;
    private EditText titleEditText;
    private EditText descriptionEditText;
    private Spinner prioritySpinner;
    private TextView taskDateTextView;
    //logic variables
    private UUID taskId;
    private Boolean isEditFrag = false;
    private Date taskDate;


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
        taskDateTextView = (TextView) view.findViewById(R.id.id_detail_view_task_date);

        String whatToDoWithIntent = (String) getArguments().getSerializable(ARG_WHAT_TO_DO_WITH_INTENT);
        taskId = (UUID) getArguments().getSerializable(ARG_TASK_ID);

        handleWhatToDoWithIntent(view, whatToDoWithIntent, taskId);

        //create onClicks
        createViewOnclicks(view);

        return view;


    }
    private Task setViewInputsIntoTask(Boolean isThisNewTask, Task taskToBeSet){

        taskToBeSet.setTitle(titleEditText.getText().toString());
        taskToBeSet.setDescription(descriptionEditText.getText().toString());
        taskToBeSet.setPriority(prioritySpinner.getSelectedItem().toString());
        taskToBeSet.setTask_date(taskDate);
        if(isThisNewTask){
            taskToBeSet.setDate_created(new Date());
            taskToBeSet.setIs_done(false);
        }
        return taskToBeSet;
    }
    private void handleWhatToDoWithIntent(View view, String whatToDoWithIntent, final UUID taskId){

        String toolbarTitle = new String();
        //if it's an add new task, set visible the Create New Task Button
        if(whatToDoWithIntent.equals(getString(R.string.app_constant_create_new_task))){
            toolbarTitle = getString(R.string.title_create_a_new_task);
            //set initial temp date as null / Date(0) until changes by the user
            updateTaskDate(new Date(0));

            createTaskButton = (Button) view.findViewById(R.id.id_detail_view_create_task_button);
            createTaskButton.setVisibility(View.VISIBLE);
            createTaskButton.setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View view) {
                    Task newTask = setViewInputsIntoTask(true, new Task());
                    long insertStatus = TaskLab.get(getActivity()).addTask(newTask);
                    if(insertStatus != -1){
                        toastAway(true);
                    }
                    else{
                        toastAway(false);
                    }
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
            //Put Update Button
            handleUpdateButtonIsTrue(view);
        }


        //Update ToolBar Title accordingly.
        handleAppCompatToolbar(toolbarTitle);

    }

    private void handleUpdateButtonIsTrue(View view) {
        updateTaskButton = (Button) view.findViewById(R.id.id_detail_view_update_task_button);
        updateTaskButton.setVisibility(View.VISIBLE);
        updateTaskButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                Task taskToBeUpdated = TaskLab.get(getActivity()).getTask(taskId);
                int updateStatus = TaskLab.get(getActivity()).updateTask(setViewInputsIntoTask(false, taskToBeUpdated));
                if(updateStatus > 0){
                    toastAway(true);
                }
                else{
                    toastAway(false);
                }
                getActivity().finish();
            }
        });
    }
    private void toastAway(boolean isSuccess){
        if(isSuccess){
            Toast.makeText(getActivity(), "Success", Toast.LENGTH_SHORT).show();
        }
        else{
            Toast.makeText(getActivity(), "Error", Toast.LENGTH_SHORT).show();
        }
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
        taskDateTextView.setText(CommonLibrary.handleModelToViewDate(getActivity(), selectedTask.getTask_date()));
        taskDate = selectedTask.getTask_date();
//        handleToViewDate()
    }
//    public String handleToViewDate(String date){
//        if(date.equals(new Date(0).toString())){
//            return "Date Not Specified";
//        }
//        else{
//            return date;
//        }
//    }
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
                int deleteStatus = TaskLab.get(getActivity()).deleteTask(taskId);
                if(deleteStatus != 0){
                    toastAway(true);
                }
                else{
                    toastAway(false);
                }
                getActivity().finish();
                return true;
            default:return super.onOptionsItemSelected(item);
        }


    }
    public void createViewOnclicks(View view){

        //Onclick on the Task Date Button
        taskDateTextView.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                FragmentManager fm = getFragmentManager();
                DatePickerFragment datePickerDialog = DatePickerFragment.newInstance(taskDate);

                //set the current fragment as the target fragment so that message is recieved by this fragment when datepicker fragment closes
                datePickerDialog.setTargetFragment(TaskDetailFragment.this, REQUEST_DATE);
                datePickerDialog.show(fm, DIALOG_DATE);
            }
        });
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent intent) {
        if(resultCode != Activity.RESULT_OK){
          return;
        }
        if(requestCode == REQUEST_DATE){
            Date date = (Date) intent.getSerializableExtra(DatePickerFragment.EXTRA_DATE);
            updateTaskDate(date);
        }
//        super.onActivityResult(requestCode, resultCode, data);
    }
    public void updateTaskDate(Date date){
        taskDate = date;
        taskDateTextView.setText(CommonLibrary.handleModelToViewDate(getActivity(), date));
    }
}
