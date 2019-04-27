package tasku.apps.vaibhavbansal.tasku.database;

import java.util.Date;
import java.util.UUID;

/**
 * Created by VAIBHAV on 7/18/2016.
 */
//Basic DBMS Table Schema
public class TaskDBSchema {
    public static final class AllTasksTable{
        public static final String NAME = "all_tasks_table";

        public static final class Cols{
            public static final String UUID = "uuid";
            public static final String TITLE = "title";
            public static final String DESCRIPTION = "description";
            public static final String TASK_DATE = "task_date";
            public static final String PRIORITY = "priority";
            public static final String IS_DONE = "is_done";
            public static final String DATE_CREATED = "date_created";
            public static final String DATE_DONE = "date_done";
        }
    }
}
