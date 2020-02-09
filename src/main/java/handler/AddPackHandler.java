package handler;

import database.models.dao.PackHandler;
import model.Pack;

import java.util.Arrays;
import java.util.List;

public class AddPackHandler {

    public void add(String keyWords, String answer) {
        callAddHandler(keyWords, answer);
    }

    private void callAddHandler(String keyWords, String answer) {
        List<String> keyWordsList = restructureKeyWords(keyWords);
        PackHandler packHandler = new PackHandler();
        for (String key: keyWordsList) {
            packHandler.add(new Pack(key, answer));
        }
    }

    private List<String> restructureKeyWords(String keyWords) {
        String[] arrayOfKeyWords = keyWords.split(";");
        return Arrays.asList(arrayOfKeyWords);
    }
}
