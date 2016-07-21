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
import android.widget.TimePicker;

import java.util.Calendar;
import java.util.Date;

/**
 * Created by VAIBHAV on 7/21/2016.
 */
public class TimePickerFragment extends DialogFragment {

    public static final String EXTRA_HOUR = "hour";
    public static final String EXTRA_MIN = "min";
    private static final String ARG_DATE_FOR_TIME = "time";
    private TimePicker timePicker;


    public static TimePickerFragment newInstance(Date date){
        Bundle args = new Bundle();
        args.putSerializable(ARG_DATE_FOR_TIME, date);
        TimePickerFragment fragment = new TimePickerFragment();
        fragment.setArguments(args);
        return fragment;
    }


    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {

        Date date = (Date)getArguments().getSerializable(ARG_DATE_FOR_TIME);
        Calendar c = CommonLibrary.setCalendarFromMilliSec(date.getTime());
        int hour = c.get(Calendar.HOUR_OF_DAY);
        int minute = c.get(Calendar.MINUTE);

        View v = LayoutInflater.from(getActivity()).inflate(R.layout.dialog_time, null);

        timePicker = (TimePicker) v.findViewById(R.id.id_dialog_time_time_picker);
        timePicker.setCurrentHour(hour);
        timePicker.setCurrentMinute(minute);




        return new AlertDialog.Builder(getActivity()).setView(v).setTitle("Choose Time").setPositiveButton(android.R.string.ok, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                int hour = timePicker.getCurrentHour();
                int minute = timePicker.getCurrentMinute();
                sendResult(Activity.RESULT_OK, hour, minute);
            }
        }).create();

    }

    public void sendResult(int resultCode, int hour, int minute){
        if(getTargetFragment() == null){
            return;
        }
        Intent intent = new Intent();
        intent.putExtra(EXTRA_HOUR, hour);
        intent.putExtra(EXTRA_MIN, minute);
        getTargetFragment().onActivityResult(getTargetRequestCode(), resultCode, intent);
    }
}
