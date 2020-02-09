package model;

public class Key extends Model{
    int id;
    String text;
    int answer_id;

    public Key(int id, String text, int answer_id) {
        this.id = id;
        this.text = text;
        this.answer_id = answer_id;
    }

    @Override
    public int getId() {
        return id;
    }

    @Override
    public void setId(int id) {
        this.id = id;
    }

    @Override
    public String getText() {
        return text;
    }

    @Override
    public void setText(String text) {
        this.text = text;
    }

    public int getAnswer_id() {
        return answer_id;
    }

    public void setAnswer_id(int answer_id) {
        this.answer_id = answer_id;
    }
}