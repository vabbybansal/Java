package tasku.apps.vaibhavbansal.tasku;

import android.app.AlarmManager;
import android.app.IntentService;
import android.app.Notification;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.res.Resources;
import android.media.RingtoneManager;
import android.os.SystemClock;
import android.os.Vibrator;
import android.support.v4.app.NotificationManagerCompat;
import android.support.v4.app.NotificationCompat;
import android.util.Log;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.UUID;

/**
 * Created by VAIBHAV on 7/25/2016.
 */
public class TaskuBackgroundService extends IntentService {
    public static final String TAG = "Tasku_Background_Service";
    public static final String TASKU_SERVICE = "tasku.apps.vaibhavbansal.tasku.background_service";
    public static final String EXTRA_TASK_UUID = "tasku.apps.vaibhavbansal.tasku.background_service_uuid";
//    public static final String EXTRA_TASK_DATE= "tasku.apps.vaibhavbansal.tasku.background_service_date";

    private static final int POLL_INTERVAL = 1000 * 60;

    public static Intent newIntent(Context context, Task taskForAlarm){
        Intent intent = new Intent(context, TaskuBackgroundService.class);
        intent.putExtra(TaskuBackgroundService.EXTRA_TASK_UUID, taskForAlarm.getUuid());
//        intent.setAction(TaskuBackgroundService.TASKU_SERVICE);
        return intent;
    }

    public static Intent newIntent(Context context){
        Intent intent = new Intent(context, TaskuBackgroundService.class);

//        intent.setAction(TaskuBackgroundService.TASKU_SERVICE);
        return intent;
    }

    public TaskuBackgroundService(){
        super(TAG);
    }

    @Override
    protected void onHandleIntent(Intent intent) {
//        Log.i(TAG, "Received an intent:" + intent);
//        Log.i(TAG, "Recieved " + intent.getSerializableExtra(EXTRA_TASK_TITLE));

        UUID taskId = (UUID) intent.getSerializableExtra(EXTRA_TASK_UUID);
        Task alarmedTask = TaskLab.get(this).getTask(taskId);
//        Resources resources = getResources();
//        Intent i = TaskDetailActivity.newIntent(this,getString(R.string.app_constant_show_existing_task), taskId);
//
//        PendingIntent pi = PendingIntent.getActivity(this, 0, i, 0);

        Notification notification = new NotificationCompat.Builder(this)
                .setTicker(getString(R.string.title_your_task))
                .setSmallIcon(R.drawable.ic_notif_icon)
                .setContentTitle(alarmedTask.getTitle())
                .setContentText(CommonLibrary.handleModelToViewTime(this,alarmedTask.getTask_date()) + ", " + CommonLibrary.handleModelToViewDate(this, alarmedTask.getTask_date()))
                .setVibrate(new long[]{1000,1000,1000,1000,1000})
                .setSound(RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION))
                .build();
        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this);
        notificationManager.notify(0, notification);
    }

    //Alarm Manager handled service
    public static void setServiceAlarm (Context context, boolean isOn){

        Task taskToBeAlarmed = getLatestTask(context);

//        if task date is in the past, then return


        boolean alarmStatus = isServiceAlarmOn(context);
        Intent i = TaskuBackgroundService.newIntent(context, taskToBeAlarmed);
//        checkIfAlarmAlreadyUp(context, i);

        //create pending intent that starts my service
        //arguments to getService = (
        //                              Context which sends the intent,
        //                              Request Code that differentiates this Pending Request from others)
        //                              The intent object to send
        //                              Flags to tweak how Pending Request is created
        //                          )
        PendingIntent pi = PendingIntent.getService(context, 0, i, 0);
        AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
        if(taskToBeAlarmed == null){
            flushAlarms(alarmManager, pi);
            return;
        }
        //no alarm in stack
        if(!alarmStatus){
            //Arguments to setInexactRepeating =>
            //  1) a constant to describe the time basis for the alarm
            //  2) Time at which to start the alarm
            //  3) The time interval at which to trigger the alarm
            //  4) Pending Intent

            //If time has to be updated code to come here

        }
        else{
            //an alarm already in stack
            flushAlarms(alarmManager, pi);
            pi = PendingIntent.getService(context, 0, i, 0);
        }
        alarmManager.set(AlarmManager.RTC_WAKEUP, taskToBeAlarmed.getTask_date().getTime(), pi);
    }

    public static void flushAlarms(AlarmManager alarmManager, PendingIntent pi){
        alarmManager.cancel(pi);
        pi.cancel();
    }

    public static boolean isServiceAlarmOn(Context context){
        Intent i = TaskuBackgroundService.newIntent(context);
        PendingIntent pi = PendingIntent.getService(context, 0, i, PendingIntent.FLAG_NO_CREATE);
        return pi != null;
    }
    public static Task getLatestTask(Context context){
        List<Task> allTasks = TaskLab.get(context).getTasksFromDB();
        SortedSet<Date> allDates = new TreeSet<Date>();
        Task latestTask = null;
        for(int i=0; i<allTasks.size(); i++){
            Date d = allTasks.get(i).getTask_date();
            //Time not starting time nor time should be in past
            if(d.getTime() != new Date(0).getTime() && d.after(new Date())){
                allDates.add(d);
                if(d.equals(allDates.first())){
                    latestTask = allTasks.get(i);
                }
            }
        }

        return latestTask;

    }

}
