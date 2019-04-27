package tasku.apps.vaibhavbansal.tasku.database;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

/**
 * Created by VAIBHAV on 7/18/2016.
 */
//Basic BoilerPlate Code for SQL Lite DB
public class TaskBaseHelper extends SQLiteOpenHelper {
    private static final int VERSION = 1;
    private static final String DATABASE_NAME = "taskU.db";

    public TaskBaseHelper(Context context){
        super(context, DATABASE_NAME, null, VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase) {
        sqLiteDatabase.execSQL(
         "create table " + TaskDBSchema.AllTasksTable.NAME + "("
        + " _id integer primary key autoincrement, "
        + TaskDBSchema.AllTasksTable.Cols.UUID + ", "
        + TaskDBSchema.AllTasksTable.Cols.TITLE + ", "
        + TaskDBSchema.AllTasksTable.Cols.DESCRIPTION + ", "
        + TaskDBSchema.AllTasksTable.Cols.TASK_DATE + ", "
        + TaskDBSchema.AllTasksTable.Cols.PRIORITY + ", "
        + TaskDBSchema.AllTasksTable.Cols.IS_DONE + ", "
        + TaskDBSchema.AllTasksTable.Cols.DATE_CREATED + ", "
        + TaskDBSchema.AllTasksTable.Cols.DATE_DONE
        + ")");
    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, int oldVersion, int newVersion) {

    }
}
