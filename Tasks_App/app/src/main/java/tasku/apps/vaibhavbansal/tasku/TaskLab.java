package tasku.apps.vaibhavbansal.tasku;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

import java.util.ArrayList;
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

    private TaskCursorWrapper queryTasks(String whereClause, String[] whereArgs, String orderBy){
        Cursor cursor = sqLiteDatabase.query(
                TaskDBSchema.AllTasksTable.NAME,
                null,//Cols to select. null selects all cols
                whereClause,
                whereArgs,
                null,
                null,
                orderBy
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
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.TASK_DATE, CommonLibrary.handleDateToMilliseconds(task.getTask_date()));
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.PRIORITY, task.getPriority());
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.IS_DONE, task.getIs_done() ? "yes" : "no");
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.DATE_CREATED, CommonLibrary.handleDateToMilliseconds(task.getDate_created()));
        contentValues.put(TaskDBSchema.AllTasksTable.Cols.DATE_DONE, CommonLibrary.handleDateToMilliseconds(task.getDate_done()));




        return contentValues;

    }

    //write tasks by first preparing the contentValues
    public long addTask(Task task){
        ContentValues contentValues = getContentValues(task);
        return(sqLiteDatabase.insert(TaskDBSchema.AllTasksTable.NAME, null, contentValues));
    }

    //update a previous task
    public int updateTask(Task task){
        String uuidString = task.getUuid().toString();
        //create contentvalues for write
        ContentValues contentValues = getContentValues(task);
        //Update
        return(sqLiteDatabase.update(TaskDBSchema.AllTasksTable.NAME, contentValues, TaskDBSchema.AllTasksTable.Cols.UUID + " = ?", new String[]{uuidString}));
    }

    //delete a previous task
    public int deleteTask(UUID taskId){
        String uuidString = taskId.toString();
        return this.deleteTask(uuidString);
    }
    public int deleteTask(String uuidString){
        return(sqLiteDatabase.delete(TaskDBSchema.AllTasksTable.NAME, TaskDBSchema.AllTasksTable.Cols.UUID + " = ?", new String[]{uuidString}));
    }

    public List<Task> getTasksFromDB(){
        List<Task> tasks = new ArrayList<>();

        //Retrieve only tasks that are incomplete
//        TaskCursorWrapper cursor = queryTasks(TaskDBSchema.AllTasksTable.Cols.IS_DONE + " = ?", new String[]{"no"} );
        TaskCursorWrapper cursor = queryTasks(TaskDBSchema.AllTasksTable.Cols.IS_DONE + " = ?", new String[]{"no"}, new String(TaskDBSchema.AllTasksTable.Cols.TASK_DATE + " ASC") );


//        TaskCursorWrapper cursor = queryTasks(null, null);
//
//        Cursor cursor1 = sqLiteDatabase.query(
//                TaskDBSchema.AllTasksTable.Cols.IS_DONE,
//                null,//Cols to select. null selects all cols
//                TaskDBSchema.AllTasksTable.Cols.IS_DONE + " = ?",
//                new String[]{"no"},
//                null,
//                null,
//                null
//        );
//        TaskCursorWrapper cursor = (TaskCursorWrapper);


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
