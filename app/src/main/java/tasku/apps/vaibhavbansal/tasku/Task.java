package tasku.apps.vaibhavbansal.tasku;

import java.util.Date;
import java.util.UUID;

/**
 * Created by VAIBHAV on 7/17/2016.
 */
public class Task {
    private UUID uuid;
    private String title;
    private String description;
    private Date task_date;
    private String priority;
    private Boolean is_done;
    private Date date_created;
    private Date date_done;
    //constructors
    public Task() {
        this(UUID.randomUUID());
    }

    public Task(UUID uuid) {
        this.uuid = uuid;
    }
    //getter setter
    public UUID getUuid() {
        return uuid;
    }

    public void setUuid(UUID uuid) {
        this.uuid = uuid;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Date getTask_date() {
        return task_date;
    }

    public void setTask_date(Date task_date) {
        this.task_date = task_date;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getPriority() {
        return priority;
    }

    public void setPriority(String priority) {
        this.priority = priority;
    }

    public Boolean getIs_done() {
        return is_done;
    }

    public void setIs_done(Boolean is_done) {
        this.is_done = is_done;
    }

    public Date getDate_created() {
        return date_created;
    }

    public void setDate_created(Date date_created) {
        this.date_created = date_created;
    }

    public Date getDate_done() {
        return date_done;
    }

    public void setDate_done(Date date_done) {
        this.date_done = date_done;
    }
}

