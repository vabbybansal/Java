package tasku.apps.vaibhavbansal.tasku;

import android.content.Context;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

import java.util.ArrayList;
import java.util.Date;
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
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_task_list, container, false);

        //Wire up the RecyclerView
        recyclerView =(RecyclerView) v.findViewById(R.id.id_recyclerView_task_list);
        recyclerView.setLayoutManager(new LinearLayoutManager(getActivity()));

        //connect the adapter with the recyclerview in the Method named ConnectRecyclerViewAdapter
        connectRecyclerViewAndAdapter();

        return v;
    }

    private void connectRecyclerViewAndAdapter(){
//        if(taskAdapter == null){

                List<Task> dummyTasks = new ArrayList<>();

                for(int i=0;i<10;i++){
                    Task task = new Task("Task - " + i, "Karle bhai nhi toh khatam hai bey tuu", new Date(),true, "Very High" );
                    dummyTasks.add(task);

                }

                taskAdapter = new TaskAdapter(dummyTasks);
                recyclerView.setAdapter(taskAdapter);
//        }
//        else{
//            taskAdapter.setMyTasks(allTasks);
//            taskAdapter.notifyDataSetChanged();
//        }
    }

    private class TaskHolder extends RecyclerView.ViewHolder{

        private TextView title;
        private TextView date;
        private TextView description;
        private TextView priority;

        private TaskHolder(View itemView) {
            super(itemView);

            //Assign TaskHolder member mimic variables to the actual Elements on the View of the List
            title = (TextView)itemView.findViewById(R.id.id_task_title);
            date = (TextView)itemView.findViewById(R.id.id_task_date);
            description = (TextView)itemView.findViewById(R.id.id_task_description);
            priority = (TextView)itemView.findViewById(R.id.id_task_priority);
        }
            //Bind the actual data to the view object
        public void bindMyTask(Task task){
            title.setText(task.getTitle());
            date.setText(task.getDate().toString());
            description.setText(task.getDescription());
            priority.setText(task.getPriority());
        }
    }
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

}
