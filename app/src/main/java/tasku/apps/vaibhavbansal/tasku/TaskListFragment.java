package tasku.apps.vaibhavbansal.tasku;

import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.app.AlertDialog;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;

/**
 * Created by VAIBHAV on 7/17/2016.
 */
public class TaskListFragment extends Fragment {

    //this view includes a list created using the recyclerview
    private RecyclerView recyclerView;
    private TaskAdapter taskAdapter;
    List<Task> allTasks;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //Will have a menu and will recieve Menu Call Backs
        setHasOptionsMenu(true);

        /////////////////////////
        /////////////////////////


    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_task_list, container, false);

        //Instantiate the Recycler view
        recyclerView =(RecyclerView) v.findViewById(R.id.id_recyclerView_task_list);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));

        //connect the adapter with the recyclerview in the Method named ConnectRecyclerViewAdapter
        connectRecyclerViewAndAdapter();

        return v;
    }

    private void connectRecyclerViewAndAdapter(){

        //get Tasks from DB using TaskLab helper class
        TaskLab taskLab = TaskLab.get(getActivity());
        allTasks = taskLab.getTasksFromDB();

        if(taskAdapter == null){


                taskAdapter = new TaskAdapter(allTasks);
                recyclerView.setAdapter(taskAdapter);
        }
        else{
            //recheck the data from DB in case an activity was created / destroyed. Make the same representation in the List View
            taskAdapter.setMyTasks(allTasks);
            taskAdapter.notifyDataSetChanged();
        }
    }

    @Override
    public void onResume() {
        super.onResume();
        //Update data to adapter when the activity is resumed from some other activity
        connectRecyclerViewAndAdapter();
    }

    //View Holder of the RecyclerView
    private class TaskHolder extends RecyclerView.ViewHolder implements View.OnClickListener{

        private Task bindedTask;
        private TextView title;
        private TextView description;
        private TextView task_date;
        private TextView priority;
        private TextView task_time;
        private CheckBox isDone;

        private TaskHolder(View itemView) {
            super(itemView);

            //set item to be give onclick callbacks
            itemView.setOnClickListener(this);

            //Assign TaskHolder member mimic variables to the actual Elements on the View of the List
            title = (TextView)itemView.findViewById(R.id.id_task_title);
            task_date = (TextView)itemView.findViewById(R.id.id_task_date);
            description = (TextView)itemView.findViewById(R.id.id_task_description);
            priority = (TextView)itemView.findViewById(R.id.id_task_priority);
            task_time = (TextView) itemView.findViewById(R.id.id_task_time);
            isDone = (CheckBox) itemView.findViewById(R.id.id_list_item_checkBox);

            //set on click on checkbox too
            isDone.setOnClickListener(this);
        }
            //Bind the actual data to the view object
        public void bindMyTask(Task task){
            bindedTask = task;
            title.setText(task.getTitle());
            task_date.setText(CommonLibrary.handleModelToViewDate(getActivity(), task.getTask_date()));
            task_time.setText(CommonLibrary.handleModelToViewTime(getActivity(), task.getTask_date()));
            description.setText(task.getDescription());
            priority.setText(task.getPriority());
            isDone.setChecked(task.getIs_done());
        }
        //Onclick handler to the item in the list view

        @Override
        public void onClick(final View view) {
//            Toast.makeText(getActivity(), bindedTask.getTitle(), Toast.LENGTH_SHORT).show();

            if(view.getId() == isDone.getId()){

                AlertDialog.Builder builder = new AlertDialog.Builder(getActivity());
                builder
                        .setTitle(getString(R.string.label_are_you_share_task_complete))
                        .setPositiveButton(android.R.string.yes, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                                setTaskUpdate(view, bindedTask, getAdapterPosition());
                            }
                        })
                        .setNegativeButton(android.R.string.no, new DialogInterface.OnClickListener() {
                            @Override
                            public void onClick(DialogInterface dialogInterface, int i) {
                                CheckBox v = (CheckBox) view;
                                v.setChecked(false);
                            }
                        })
                        .show();
            }
            else{
                Intent intent = TaskDetailActivity.newIntent(getActivity(), getString(R.string.app_constant_show_existing_task) ,bindedTask.getUuid());
                startActivity(intent);
            }
        }

        private void setTaskUpdate(View view, Task bindedTask, int bindedPosition){
            //set Done in DB
            CheckBox v = (CheckBox) view;
            bindedTask.setIs_done(v.isChecked());
            TaskLab.get(getActivity()).updateTask(bindedTask);
            CommonLibrary.updateAlarmManager(getActivity());
            //remove the done list item from the list. bindedPosition is accessed through getAdapterPosition()
            removeTaskFromView(bindedPosition);
        }
        public void removeTaskFromView(int bindedPosition){
            //remove the task from the logical model(not DB) from which the Recycler View was generated
            allTasks.remove(bindedPosition);
            //notify the Adapter that the Item an item has been removed from its logical model data set
            taskAdapter.notifyItemRemoved(bindedPosition);
            taskAdapter.notifyItemRangeChanged(bindedPosition, allTasks.size());
        }
    }
    //Adapter of the RecyclerView
    private class TaskAdapter extends RecyclerView.Adapter<TaskHolder>{

        private List<Task> allTasks;

        private TaskAdapter(List<Task> allTasks) {
            this.allTasks = allTasks;
        }

        //create The Viewholder (View object with the model data filled in (its own implementation->check above))
        @Override
        public TaskHolder onCreateViewHolder(ViewGroup viewGroup, int i) {
            //inflate list item and create the corresponding TaskHolder
            LayoutInflater layoutInflater = LayoutInflater.from(getActivity());
            View view = layoutInflater.inflate(R.layout.item_task_list, viewGroup, false);

            return new TaskHolder(view);
        }

        @Override
        public void onBindViewHolder(TaskHolder taskHolder, int position) {
            //Fetch the required Task using the position
            Task task = allTasks.get(position);

            //bind the list item to a task. Works when a list item is clicked -> binds the corresponding task object
            taskHolder.bindMyTask(task);
        }

        @Override
        public int getItemCount() {
            return allTasks.size();
        }

        public void setMyTasks(List<Task> allTasks){
            this.allTasks = allTasks;
        }

    }


    //Menu Options Override Functions
    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        super.onCreateOptionsMenu(menu, inflater);
        inflater.inflate(R.menu.fragment_task_list_inbox, menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {

        switch (item.getItemId()){

            case R.id.id_menu_item_new_task:
                //Task newTask = new Task();
                //TaskLab.get(getActivity()).addTask(newTask);
                //Start a plain Detail Activity for creating a new Task
                Intent intent = TaskDetailActivity.newIntent(getActivity(),getString(R.string.app_constant_create_new_task), null);
                startActivity(intent);
                return true;

            default:return super.onOptionsItemSelected(item);
        }


    }
}
