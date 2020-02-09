package database.models.dao;

import database.Database;
import database.models.PackDao;
import model.Answer;
import model.Key;
import model.Pack;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class PackHandler implements PackDao {
    private Database database = Database.getInstance();
    private String addAnswerSql = "INSERT INTO answer (text) VALUE (?)";
    private String updateAnswerSql = "UPDATE answer SET text = ? WHERE id = ?";
    private String deleteAnswerSql = "DELETE FROM answer WHERE id = ?";
    private String addKeyWordSql = "INSERT INTO `key` (text, answer_id) VALUE (?, ?)";
    private String updateKeyWordSql = "UPDATE `key` SET text = ? WHERE answer_id = ?";
    private String deleteKeyWordSql = "DELETE FROM `key` WHERE id = ?";
    private String selectAnswerByIdSql = "SELECT * FROM answer WHERE id = ?";
    private String selectAnswerByTextSql = "SELECT * FROM answer WHERE text LIKE ?";
    private String selectKeyWordByIdSql = "SELECT * FROM `key` WHERE id = ?";
    private String selectKeyWordByTextSql = "SELECT * FROM `key` WHERE text = ?";
    private String selectKeyWordByAnswerIdSql = "SELECT * FROM `key` WHERE answer_id = ?";
    private String selectAnswerWithKeySorted = "SELECT answer.text as answer, `key`.text as key_word FROM answer JOIN `key` ON answer.id = `key`.answer_id ORDER BY ?";
    private String selectAnswerWithKey = "SELECT `answer.text as answer, `key`.text as key_word FROM answer JOIN `key` ON answer.id = `key`.answer_id WHERE answer.id = ?";
    private String selectAllAnswerWithKey = "SELECT DISTINCT answer.text as answer, `key`.text as key_word FROM answer JOIN `key` ON answer.id = `key`.answer_id";

    public boolean add(Pack pack) {
        try {
            PreparedStatement statementAddAnswerSql = database.getConnection().prepareStatement(addAnswerSql);
            statementAddAnswerSql.setString(1, pack.getAnswer());
            statementAddAnswerSql.executeUpdate();
            statementAddAnswerSql.close();
            database.closeConnection();
            PreparedStatement statementSelectByText = database.getConnection().prepareStatement("%" + selectAnswerByTextSql + "%");
            statementSelectByText.setString(1, pack.getAnswer());
            ResultSet answer = statementSelectByText.executeQuery();
            int id = 0;
            while (answer.next()) {
                id = answer.getInt("id");
            }
            answer.close();
            statementSelectByText.close();
            database.closeConnection();
            PreparedStatement statementAddKeyWord = database.getConnection().prepareStatement(addKeyWordSql);

            statementAddKeyWord.setString(1, pack.getKeyWord());
            statementAddKeyWord.setInt(2, id);
            statementAddAnswerSql.executeUpdate();
            statementAddKeyWord.close();
            database.closeConnection();
        } catch (SQLException e) {
            throw new IllegalStateException(e);
        }
        return true;
    }

    public boolean updateAnswer(Answer answer) {
        try {
            PreparedStatement statementUpdateAnswerSql = database.getConnection().prepareStatement(updateAnswerSql);
            statementUpdateAnswerSql.setInt(1, answer.getId());
            statementUpdateAnswerSql.executeUpdate();
            statementUpdateAnswerSql.close();
            database.closeConnection();
        } catch (SQLException e) {
            throw new IllegalStateException(e);
        }
        return true;
    }

    public boolean updateKey(Answer answer, String key) {
        try {
            int answer_id = 0;

            PreparedStatement statementSelectId = database.getConnection().prepareStatement(selectAnswerByTextSql);
            statementSelectId.setString(1, "%" + answer.getText() + "%");
            ResultSet selectId = statementSelectId.executeQuery();
            while (selectId.next()) {
                answer_id = selectId.getInt("id");
            }
            selectId.close();
            statementSelectId.close();
            database.closeConnection();

            PreparedStatement statementUpdateKeySql = database.getConnection().prepareStatement(updateKeyWordSql);
            statementUpdateKeySql.setString(1, key);
            statementUpdateKeySql.setInt(2, answer_id);
            statementUpdateKeySql.executeUpdate();
            statementUpdateKeySql.close();
            database.closeConnection();
        } catch (SQLException e) {
            throw new IllegalStateException(e);
        }
        return true;
    }

    public boolean delete(Pack pack) {
        return false;
    }

    public Collection<Pack> getAllPacks() {
        List<Pack> packList = new ArrayList();
        try {
            PreparedStatement statementSelect = database.getConnection().prepareStatement(selectAllAnswerWithKey);

            ResultSet resultSet = statementSelect.executeQuery();

            while (resultSet.next()) {
                packList.add(new Pack(resultSet.getString("key_word"), resultSet.getString("answer")));
            }
        } catch (SQLException e) {
            throw new IllegalStateException(e);
        }
        return packList;
    }
}
