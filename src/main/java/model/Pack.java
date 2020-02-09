package model;

public class Pack {
    private String keyWord;
    private String answer;
    private int answer_id;
    private int key_id;

    public Pack(String keyWord, String answer, int answer_id, int key_id) {
        this.keyWord = keyWord;
        this.answer = answer;
        this.answer_id = answer_id;
        this.key_id = key_id;
    }

    public Pack(String keyWord, String answer) {
        this.keyWord = keyWord;
        this.answer = answer;
    }

    public int getAnswer_id() {
        return answer_id;
    }

    public void setAnswer_id(int answer_id) {
        this.answer_id = answer_id;
    }

    public int getKey_id() {
        return key_id;
    }

    public void setKey_id(int key_id) {
        this.key_id = key_id;
    }

    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }

    public String getKeyWord() {
        return keyWord;
    }

    public void setKeyWord(String keyWord) {
        this.keyWord = keyWord;
    }
}
