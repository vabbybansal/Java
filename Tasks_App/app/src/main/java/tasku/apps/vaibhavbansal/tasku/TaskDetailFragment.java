package tasku.apps.vaibhavbansal.tasku;

import android.app.Activity;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Calendar;
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

    //dummy dumm
    private static final String DIALOG_TIME = "DialogTime";
    private static final int REQUEST_TIME = 1;

    //Onscreen Rotation save instance state final strings
    private static final String SAVED_TITLE = "saved_title";
    private static final String SAVED_DESCRIPTION = "saved_description";
    private static final String SAVED_TASK_DATE = "saved_task_date";
    private static final String SAVED_PRIORITY = "saved_priority";

    //View Variables
    private Button createTaskButton;
    private Button updateTaskButton;
    private Button completeButton;
    private EditText titleEditText;
    private EditText descriptionEditText;
    private Spinner prioritySpinner;
    private TextView taskDateTextView;
    private TextView timePickerTextView;

    //logic variables
    private UUID taskId;
    private Boolean isEditFrag = false;
    private Date taskDate = CommonLibrary.getZeroDate();
    private int taskHour;
    private int taskMinute;
    private String whatIntentWants;
    private int isRotated;


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
        timePickerTextView = (TextView) view.findViewById(R.id.id_detail_view_task_time);
        //
//        updateTaskDate(new Date(0));
        if(savedInstanceState != null){
            myRestoreInstanceState(savedInstanceState);
            isRotated = 1;
        }

        String whatToDoWithIntent = (String) getArguments().getSerializable(ARG_WHAT_TO_DO_WITH_INTENT);
        whatIntentWants = whatToDoWithIntent;
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
                    CommonLibrary.updateAlarmManager(getActivity());
                    getActivity().finish();
                }
            });


        }
        //if it is an edit task
        else if (whatToDoWithIntent.equals(getString(R.string.app_constant_show_existing_task))){
            toolbarTitle = " " + getString(R.string.title_edit_task);
            isEditFrag = true;
            Task selectedTask = TaskLab.get(getActivity()).getTask(taskId);
            if(isRotated != 1){
                populateFields(selectedTask);
            }

            //Put Update Button
            handleUpdateButtonIsTrue(view);
            handleCompleteButtonIsTrue(view);
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

                AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
                builder
                        .setTitle(getString(R.string.sure_you_want_to_update))
                        .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                                Task taskToBeUpdated = TaskLab.get(getActivity()).getTask(taskId);
                                int updateStatus = TaskLab.get(getActivity()).updateTask(setViewInputsIntoTask(false, taskToBeUpdated));
                                if (updateStatus > 0) {
                                    toastAway(true);
                                } else {
                                    toastAway(false);
                                }
                                CommonLibrary.updateAlarmManager(getActivity());
                                getActivity().finish();

                            }
                        })
                        .setNegativeButton(android.R.string.no, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                            }
                        })
                        .show();



            }
        });

    }

    private void handleCompleteButtonIsTrue(View view){
        completeButton = (Button) view.findViewById(R.id.id_detail_view_complete_task);
        completeButton.setVisibility(View.VISIBLE);
        completeButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {


                AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
                builder
                        .setTitle(getString(R.string.sure_you_want_to_complete))
                        .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                                Task taskToBeCompleted = TaskLab.get(getActivity()).getTask(taskId);
                                taskToBeCompleted.setIs_done(true);
                                TaskLab.get(getActivity()).updateTask(taskToBeCompleted);
                                CommonLibrary.updateAlarmManager(getActivity());
                                final Handler handler = new Handler();
                                handler.postDelayed(new Runnable() {
                                    @Override
                                    public void run() {
                                        Toast.makeText(getActivity(), "Task Completed", Toast.LENGTH_SHORT).show();
                                        getActivity().finish();
                                    }
                                }, 400);
                            }
                        })
                        .setNegativeButton(android.R.string.no, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                            }
                        })
                        .show();

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
        timePickerTextView.setText(CommonLibrary.handleModelToViewTime(getActivity(), taskDate));
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

                AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
                builder
                        .setTitle(getString(R.string.sure_you_want_to_delete))
                        .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                                int deleteStatus = TaskLab.get(getActivity()).deleteTask(taskId);
                                if (deleteStatus != 0) {
                                    toastAway(true);
                                } else {
                                    toastAway(false);
                                }
                                CommonLibrary.updateAlarmManager(getActivity());
                                getActivity().finish();
                            }
                        })
                        .setNegativeButton(android.R.string.no, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                            }
                        })
                        .show();



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

        //
        timePickerTextView.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                FragmentManager fm = getFragmentManager();
                TimePickerFragment timePickerDialog = TimePickerFragment.newInstance(taskDate);

                timePickerDialog.setTargetFragment(TaskDetailFragment.this, REQUEST_TIME);
                timePickerDialog.show(fm, DIALOG_TIME);
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
        if(requestCode == REQUEST_TIME){
            taskHour = (int) intent.getSerializableExtra(TimePickerFragment.EXTRA_HOUR);
            taskMinute = (int) intent.getSerializableExtra(TimePickerFragment.EXTRA_MIN);
            putTimeInDate(taskHour, taskMinute);
        }
//        super.onActivityResult(requestCode, resultCode, data);
    }
    public void putTimeInDate(int hour, int minute){
        //if Date is not set till now and I do set a time, then set task date to today's date
        if(taskDate.before(CommonLibrary.getConstantDateToCompare())){
            taskDate = new Date();
        }
        Calendar c = CommonLibrary.setCalendarFromMilliSec(taskDate.getTime());
        c.set(Calendar.HOUR_OF_DAY, hour);
        c.set(Calendar.MINUTE, minute);
        c.set(Calendar.SECOND, 0);
//        updateTaskDate(CommonLibrary.calendarToDate(c));
        taskDate = CommonLibrary.calendarToDate(c);
        timePickerTextView.setText(CommonLibrary.handleModelToViewTime(getActivity(), taskDate));
        taskDateTextView.setText(CommonLibrary.handleModelToViewDate(getActivity(), taskDate));
    }
    public void updateTaskDate(Date date){
        //(oldDate, newDate)
        taskDate = CommonLibrary.updateOnlyDatePart(taskDate, date);
        taskDateTextView.setText(CommonLibrary.handleModelToViewDate(getActivity(), date));
    }

    //save data on screen rotation

    @Override
    public void onSaveInstanceState(Bundle outState) {

        super.onSaveInstanceState(outState);

            outState.putString(SAVED_TITLE, titleEditText.getText().toString());
            outState.putString(SAVED_DESCRIPTION, descriptionEditText.getText().toString());
            outState.putString(SAVED_PRIORITY, prioritySpinner.getSelectedItem().toString());
            outState.putLong(SAVED_TASK_DATE, taskDate.getTime());

    }

    public void myRestoreInstanceState(Bundle savedState){

        titleEditText.setText(savedState.getString(SAVED_TITLE));
        descriptionEditText.setText(savedState.getString(SAVED_DESCRIPTION));
        prioritySpinner.setSelection(getSpinnerIndex(prioritySpinner, savedState.getString(SAVED_PRIORITY)));
        long savedDate = savedState.getLong(SAVED_TASK_DATE);
        updateTaskDate(new Date(savedDate));
        timePickerTextView.setText(CommonLibrary.handleModelToViewTime(getActivity(), taskDate));
    }

}
