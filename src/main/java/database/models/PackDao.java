package database.models;

import model.Answer;
import model.Key;
import model.Pack;

import java.util.Collection;

public interface PackDao {
    boolean add(Pack pack);

    boolean updateAnswer(Answer answer);

    boolean updateKey(Answer answer, String key);

    boolean delete(Pack pack);

    Collection<Pack> getAllPacks();
}
