package tasku.apps.vaibhavbansal.tasku;

import java.util.Date;

/**
 * Created by VAIBHAV on 7/17/2016.
 */
public class Task {
    private String title;
    private String description;
    private Date date;
    
    private Boolean isDone;
    private String priority;

    public Task(String title, String description, Date date, Boolean isDone, String priority) {
        this.title = title;
        this.description = description;
        this.date = date;
        this.isDone = isDone;
        this.priority = priority;
    }

    public Task(String title, String description, Boolean isDone, String priority) {
        this.title = title;
        this.description = description;
        this.isDone = isDone;
        this.priority = priority;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public Boolean getIsDone() {
        return isDone;
    }

    public void setIsDone(Boolean isDone) {
        this.isDone = isDone;
    }

    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }
}
