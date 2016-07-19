package tasku.apps.vaibhavbansal.tasku;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.UUID;

import tasku.apps.vaibhavbansal.tasku.database.TaskBaseHelper;
import tasku.apps.vaibhavbansal.tasku.database.TaskCursorWrapper;
import tasku.apps.vaibhavbansal.tasku.database.TaskDBSchema;

/**
 * Created by VAIBHAV on 7/18/2016.
 */
public class TaskLab {
    private static TaskLab taskLab;

    private Context context;
    private SQLiteDatabase sqLiteDatabase;

    //To be Clarified
    public static TaskLab get (Context context){
        if(taskLab == null){
            taskLab = new TaskLab(context);
        }
            return taskLab;

    }

    private TaskLab(Context context){
        context = context.getApplicationContext();
        sqLiteDatabase = new TaskBaseHelper(context).getWritableDatabase();
    }

    //Read a row of task by providing whereClause and where Arguments
    private TaskCursorWrapper queryTasks(String whereClause, String[] whereArgs){
        Cursor cursor = sqLiteDatabase.query(
                TaskDBSchema.AllTasksTable.NAME,
                null,//Cols to select. null selects all cols
                whereClause,
                whereArgs,
                null,
                null,
                null
        );

        return new TaskCursorWrapper(cursor);
    }
    //get Task from the database from the provided uuid
    public Task getTask(UUID uuid){
        TaskCursorWrapper cursor = queryTasks(TaskDBSchema.AllTasksTable.Cols.UUID + " = ?", new String[]{uuid.toString()});
        try{
            if(cursor.getCount() == 0)
            {
                return null;
            }
            cursor.moveToFirst();
            return cursor.getTask();
        }finally{
            cursor.close();
        }
    }

    //Writes
    //create contentValues for the write to take place
    private static ContentValues getContentValues(Task task){
        ContentValues contentValues = new ContentValues();

        contentValues.put(TaskDBSchema.AllTasksTable.Cols.UUID, task.getUuid().toString());
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.TITLE, task.getTitle());
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.DESCRIPTION, task.getDescription());
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.TASK_DATE, handleNullDates(task.getTask_date()));
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.PRIORITY, task.getPriority());
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.IS_DONE, task.getIs_done() ? 1 : 0);
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.DATE_CREATED, handleNullDates(task.getDate_created()));
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.DATE_DONE, handleNullDates(task.getDate_done()));




        return contentValues;

    }
    private static Long handleNullDates(Date date){
        if(date == null)
        {
            return null;
        }
        else{
            return date.getTime();
        }
    }
    //write tasks by first preparing the contentValues
    public void addTask(Task task){
        ContentValues contentValues = getContentValues(task);
        sqLiteDatabase.insert(TaskDBSchema.AllTasksTable.NAME, null, contentValues);
    }

    //update a previous task
    public void updateTask(Task task){
        String uuidString = task.getUuid().toString();
        //create contentvalues for write
        ContentValues contentValues = getContentValues(task);
        //Update
        sqLiteDatabase.update(TaskDBSchema.AllTasksTable.NAME, contentValues, TaskDBSchema.AllTasksTable.Cols.UUID + " = ?", new String[]{uuidString});
    }

    public List<Task> getTasksFromDB(){
        List<Task> tasks = new ArrayList<>();
        TaskCursorWrapper cursor = queryTasks(null, null);

        try{
            cursor.moveToFirst();
            while(!cursor.isAfterLast()){
                tasks.add(cursor.getTask());
                cursor.moveToNext();
            }
        }finally{
            cursor.close();
        }
        return tasks;

    }

}
