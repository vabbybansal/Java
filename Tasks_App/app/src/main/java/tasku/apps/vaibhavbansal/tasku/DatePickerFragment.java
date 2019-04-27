package tasku.apps.vaibhavbansal.tasku;

import android.app.Activity;
import android.app.Dialog;


import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.DialogFragment;
import android.support.v7.app.AlertDialog;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.DatePicker;

import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

/**
 * Created by VAIBHAV on 7/21/2016.
 */
public class DatePickerFragment extends DialogFragment {

    private static final String ARG_DATE = "date";
    public static final String EXTRA_DATE = "tasku.apps.vaibhavbansal.tasku.date";
    private DatePicker datepicker;

    public static DatePickerFragment newInstance(Date date){
        Bundle args = new Bundle();
        args.putSerializable(ARG_DATE, date);
        DatePickerFragment fragment = new DatePickerFragment();
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {

        //Recieve the fragment argument of the task
        Date date = (Date)getArguments().getSerializable(ARG_DATE);

        //specify to Date Picker that if the date passed is null / new Date(0), then open it with today's date (new Date())
        if(date.equals(new Date(0))){
            date = new Date();
        }
//        /////////////
//        date = new Date(new Date().getTime() - (7 *  1000 * 60 * 60 * 24));
//        /////////////
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(date);
        int year = calendar.get(Calendar.YEAR);
        int month = calendar.get(Calendar.MONTH);
        int day = calendar.get(Calendar.DAY_OF_MONTH);

        //Inflate the xml source of adapter
        View v = LayoutInflater.from(getActivity()).inflate(R.layout.dialog_date, null);

        datepicker = (DatePicker) v.findViewById(R.id.dialog_date_date_picker);
        datepicker.init(year, month, day, null);
        datepicker.setMinDate(System.currentTimeMillis() - 1000);


//        return super.onCreateDialog(savedInstanceState);
        return new AlertDialog.Builder(getActivity()).setView(v).setTitle(getString(R.string.choose_task_date)).setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                int year = datepicker.getYear();
                int month = datepicker.getMonth();
                int day = datepicker.getDayOfMonth();
                Date newDate = new GregorianCalendar(year, month, day).getTime();
                sendResult(Activity.RESULT_OK, newDate);
            }
        }).create();
    }
    private void sendResult(int resultCode, Date newDate){
        if(getTargetFragment() == null){
            return;
        }
        Intent intent = new Intent();
        intent.putExtra(EXTRA_DATE, newDate);

        getTargetFragment().onActivityResult(getTargetRequestCode(), resultCode, intent);
    }
}
