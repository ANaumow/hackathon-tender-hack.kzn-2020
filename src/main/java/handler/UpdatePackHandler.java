package handler;

import database.models.dao.PackHandler;
import model.Answer;
import model.Key;
import model.Pack;

import java.util.Arrays;
import java.util.List;

public class UpdatePackHandler {
    public void update(Answer answer, String key) {
        callUpdateHandler(answer, key);
    }

    private void callUpdateHandler(Answer answer, String key) {
        List<String> keyWordsList = restructureKeyWords(key);
        PackHandler packHandler = new PackHandler();
        for (String keey: keyWordsList) {
            packHandler.updateKey(answer, keey);
        }
        packHandler.updateAnswer(answer);
    }

    private List<String> restructureKeyWords(String keyWords) {
        String[] arrayOfKeyWords = keyWords.split(";");
        return Arrays.asList(arrayOfKeyWords);
    }
}
