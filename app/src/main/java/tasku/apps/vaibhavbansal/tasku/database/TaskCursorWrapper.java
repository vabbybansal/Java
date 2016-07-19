package tasku.apps.vaibhavbansal.tasku.database;

import android.database.Cursor;
import android.database.CursorWrapper;

import java.util.Date;
import java.util.UUID;

import tasku.apps.vaibhavbansal.tasku.Task;

/**
 * Created by VAIBHAV on 7/18/2016.
 */
//Custom Class inhereting DBMS Cursor For Reading to the Database
public class TaskCursorWrapper extends CursorWrapper {
    public TaskCursorWrapper(Cursor cursor){super(cursor);}

    public Task getTask(){
        //Access Values from the cursor
        Cursor cursor = this;
        if(cursor != null)
        {
            String uuidString = getString(getColumnIndex(TaskDBSchema.AllTasksTable.Cols.UUID));
            String title = getString(getColumnIndex(TaskDBSchema.AllTasksTable.Cols.TITLE));
            String description = getString(getColumnIndex(TaskDBSchema.AllTasksTable.Cols.DESCRIPTION));
            long task_date = getLong(getColumnIndex(TaskDBSchema.AllTasksTable.Cols.TASK_DATE));
            String priority = getString(getColumnIndex(TaskDBSchema.AllTasksTable.Cols.PRIORITY));
            int is_done = getInt(getColumnIndex(TaskDBSchema.AllTasksTable.Cols.IS_DONE));
            long date_created = getLong(getColumnIndex(TaskDBSchema.AllTasksTable.Cols.DATE_CREATED));
            long date_done = getLong(getColumnIndex(TaskDBSchema.AllTasksTable.Cols.DATE_DONE));

            //Assign values to a new Task variable and return it
            Task task = new Task(UUID.fromString(uuidString));
            task.setTitle(title);
            task.setDescription(description);
            task.setTask_date(new Date(task_date));
            task.setPriority(priority);
            task.setIs_done(is_done == 1);
            task.setDate_created(new Date(date_created));
            task.setDate_done(new Date(date_done));
            return task;
        }
        else{
            return null;
        }
    }

}
