package tasku.apps.vaibhavbansal.tasku;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.List;

/**
 * Created by VAIBHAV on 7/17/2016.
 */
public class TaskListFragment extends Fragment {

    //this view includes a list created using the recyclerview
    private RecyclerView recyclerView;
    private TaskAdapter taskAdapter;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //Will have a menu and will recieve Menu Call Backs
        setHasOptionsMenu(true);
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
        List<Task> allTasks = taskLab.getTasksFromDB();

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

        private TaskHolder(View itemView) {
            super(itemView);

            //set item to be give onclick callbacks
            itemView.setOnClickListener(this);

            //Assign TaskHolder member mimic variables to the actual Elements on the View of the List
            title = (TextView)itemView.findViewById(R.id.id_task_title);
            task_date = (TextView)itemView.findViewById(R.id.id_task_date);
            description = (TextView)itemView.findViewById(R.id.id_task_description);
            priority = (TextView)itemView.findViewById(R.id.id_task_priority);
        }
            //Bind the actual data to the view object
        public void bindMyTask(Task task){
            bindedTask = task;
            title.setText(task.getTitle());
            task_date.setText(CommonLibrary.handleModelToViewDate(getActivity(),task.getTask_date()));
            description.setText(task.getDescription());
            priority.setText(task.getPriority());
        }
        //Onclick handler to the item in the list view

        @Override
        public void onClick(View view) {
//            Toast.makeText(getActivity(), bindedTask.getTitle() , Toast.LENGTH_SHORT).show();
            Intent intent = TaskDetailActivity.newIntent(getActivity(), getString(R.string.app_constant_show_existing_task) ,bindedTask.getUuid());
            startActivity(intent);
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
