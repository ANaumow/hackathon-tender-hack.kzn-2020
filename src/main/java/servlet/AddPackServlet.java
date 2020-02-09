package servlet;

import handler.AddPackHandler;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

import java.io.IOException;

@WebServlet("/add")
public class AddPackServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
        request.setCharacterEncoding("UTF-8");
        response.setCharacterEncoding("UTF-8");
        String questionKeyWordList = request.getParameter("keyWords");
        String answer = request.getParameter("answer");


        AddPackHandler addPackHandler = new AddPackHandler();
        addPackHandler.add(questionKeyWordList, answer);

        response.sendRedirect("edit");
    }

}