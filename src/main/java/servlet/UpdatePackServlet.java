package servlet;

import handler.SelectPackHandler;
import handler.UpdatePackHandler;
import model.Answer;
import model.Pack;
import utils.FreemarkerConfig;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

@WebServlet("/edit")
public class UpdatePackServlet extends HttpServlet {
    String editUrl = "edit";
    private String templateName = "temp.ftl";

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");
        Map<String, Object> root = new HashMap<>();
        //if (request.getParameter("orderBy") != null) {
        //    if (request.getParameter("orderBy").equals("id")) {
        SelectPackHandler selectPackHandler = new SelectPackHandler();
        List<Pack> packs = (List<Pack>) selectPackHandler.select();
        //packs.removeIf(x -> x.getAnswer().equals("Обновите страницу нажатием Ctrl+F5 и повторите операцию."));
        Collections.shuffle(packs);
        //request.setAttribute("packs", packs);
        //System.out.println(packs);
        root.put("packs", packs);
        //}
        //} //else {
        ////    // ordering
        //}
        FreemarkerConfig.preprocessConfig(response.getWriter(), root, getServletContext(), templateName);
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");
        String quetionKeyWordList = request.getParameter("keyWords");
        String answer_text = request.getParameter("answer_text");
        int answer_id = Integer.valueOf(request.getParameter("answer_id"));

        Answer answer = new Answer(answer_id, answer_text);

        UpdatePackHandler updatePackHandler = new UpdatePackHandler();
        updatePackHandler.update(answer, quetionKeyWordList);

        response.sendRedirect(editUrl);
    }
}
