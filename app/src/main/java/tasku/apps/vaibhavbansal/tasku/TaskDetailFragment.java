package tasku.apps.vaibhavbansal.tasku;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
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

    public static TaskDetailFragment newInstance(String whatToDoWithIntent, UUID taskId){
        //taskId is null in case of whatToDo = "Create new Task"
        Bundle args = new Bundle();
        args.putSerializable(ARG_WHAT_TO_DO_WITH_INTENT, whatToDoWithIntent);
        args.putSerializable(ARG_TASK_ID, taskId);
        TaskDetailFragment fragment = new TaskDetailFragment();
        fragment.setArguments(args);

        return fragment;

    }


    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_detailed_view, container, false);
        titleEditText = (EditText) view.findViewById(R.id.id_detail_view_task_title);
        descriptionEditText = (EditText) view.findViewById(R.id.id_detail_view_task_description);
        prioritySpinner = (Spinner) view.findViewById(R.id.id_detail_view_priority_spinner);


        String whatToDoWithIntent = (String) getArguments().getSerializable(ARG_WHAT_TO_DO_WITH_INTENT);
        UUID taskId = (UUID) getArguments().getSerializable(ARG_TASK_ID);

        handleWhatToDoWithIntent(view, whatToDoWithIntent, taskId);

        return view;


    }
    private void handleWhatToDoWithIntent(View view, String whatToDoWithIntent, final UUID taskId){
        //if it's an add new task, set visible the Create New Task Button
        if(whatToDoWithIntent.equals(getString(R.string.app_constant_create_new_task))){
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

//                    newTask.setIs_done(true);
//                    newTask.setPriority("High Priority");
//                    newTask.setTitle("Get Milk");
//                    newTask.setDescription("Nothing");
//                    newTask.setDate_done(new Date());
//                    newTask.setDate_created(new Date());
                    //newTask.setTask_date(new Date());


                    TaskLab.get(getActivity()).addTask(newTask);
                    getActivity().finish();
                }
            });


        }



    }
}
