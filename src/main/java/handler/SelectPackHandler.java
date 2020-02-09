package handler;

import database.models.dao.PackHandler;
import model.Pack;

import java.util.Collection;

public class SelectPackHandler {
    public Collection<Pack> select() {
        return selecting();
    }

    private Collection<Pack> selecting() {
        PackHandler packHandler = new PackHandler();
        return packHandler.getAllPacks();
    }
}
