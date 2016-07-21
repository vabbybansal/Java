package tasku.apps.vaibhavbansal.tasku;

import android.app.Dialog;

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

    private TimePicker timePicker;


    public static TimePickerFragment newInstance(){
//        Bundle args = new Bundle();
//        args.putSerializable(ARG_DATE, date);
//        DatePickerFragment fragment = new DatePickerFragment();
//        fragment.setArguments(args);
//        return fragment;
        TimePickerFragment fragment = new TimePickerFragment();
        return fragment;
    }


    @Override
    public Dialog onCreateDialog(Bundle savedInstanceState) {

        View v = LayoutInflater.from(getActivity()).inflate(R.layout.dialog_time, null);



        Calendar c = Calendar.getInstance();
        int hour = c.get(Calendar.HOUR_OF_DAY);
        int minute = c.get(Calendar.MINUTE);

        timePicker = (TimePicker) v.findViewById(R.id.id_dialog_time_time_picker);
        timePicker.setCurrentHour(hour);
        timePicker.setCurrentMinute(minute);




        return new AlertDialog.Builder(getActivity()).setView(v).setTitle("Choose Time").setPositiveButton(android.R.string.ok, null).create();

    }
}
