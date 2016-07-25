package tasku.apps.vaibhavbansal.tasku;

import android.content.Context;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

/**
 * Created by VAIBHAV on 7/20/2016.
 */
public class CommonLibrary {

    public static Date getZeroDate(){
        Date date = new Date(0);
        Calendar c = setCalendarFromMilliSec(date.getTime());
        c.set(Calendar.HOUR_OF_DAY, 0);
        c.set(Calendar.MINUTE, 0);
        return calendarToDate(c);
    }

    public static Date getConstantDateToCompare(){
        Calendar c = setCalendarFromMilliSec(new Date(0).getTime());
        c.add(Calendar.DAY_OF_MONTH, 2);
        return calendarToDate(c);
    }


    public static String handleModelToViewDate(Context context, Date date){

        if(date.before(getConstantDateToCompare())){
            return context.getString(R.string.label_date_not_specified);
        }
        else{
            SimpleDateFormat formatter = new SimpleDateFormat("MMM dd, yyyy");
            String stringedDate = formatter.format(date.getTime());
            return stringedDate;
        }
    }

    public static String handleModelToViewTime(Context context, Date date){
        if(date.before(getConstantDateToCompare())){
            return (context.getString(R.string.time_not_set));
        }
        else {
            SimpleDateFormat formatter = new SimpleDateFormat("h:mm a");
            String stringedTime = formatter.format(date.getTime());
            return stringedTime;
        }
    }

//    public static Date handleViewToModelDate(Context context, String date){
//        if(date.equals(context.getString(R.string.label_date_not_specified)) | date.equals(new Date(0).toString())){
//            return new Date(0);
//        }
//        else{
//            return
//        }
//    }
//Date to be stored in DB
    public static Long handleDateToMilliseconds(Date date){
        if(date == null)
        {
            return new Date(0).getTime();
        }
        else{
            return date.getTime();
        }
    }

    //Calendar to Milliseconds,  Calendar to DB
    public static long getMilliSecFromCalendar(Calendar calendar){
        return calendar.getTimeInMillis();
    }

    public static Date calendarToDate(Calendar c){
        return new Date(getMilliSecFromCalendar(c));
    }

    //Milliseconds to Calendar
    public static Calendar setCalendarFromMilliSec(long millSec){
        Calendar calendar = Calendar.getInstance();
        calendar.setTimeInMillis(millSec);
        return calendar;
    }

    public static Date updateOnlyDatePart(Date oldDate,Date newDate){
        Calendar cOld = CommonLibrary.setCalendarFromMilliSec(oldDate.getTime());
        Calendar cNew = CommonLibrary.setCalendarFromMilliSec(newDate.getTime());

        cOld.set(Calendar.DAY_OF_MONTH, cNew.get(Calendar.DAY_OF_MONTH));
        cOld.set(Calendar.MONTH, cNew.get(Calendar.MONTH));
        cOld.set(Calendar.YEAR, cNew.get(Calendar.YEAR));
        return calendarToDate(cOld);
    }



}
