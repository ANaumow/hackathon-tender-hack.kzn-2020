package utils;


import freemarker.template.*;

import javax.servlet.ServletContext;
import java.io.File;
import java.io.IOException;
import java.io.Writer;
import java.util.Locale;
import java.util.Map;

public class FreemarkerConfig {

    private static Configuration configuration;

    private FreemarkerConfig() {
    }

    public static Configuration getInstance(String realPath, ServletContext servletContext) {
        if (configuration == null) {
            configuration = new Configuration(Configuration.VERSION_2_3_29);
            configurateConfig(configuration, realPath, servletContext);
        }
        return configuration;
    }

    private static void configurateConfig(Configuration configuration, String pathToTemplates, ServletContext servletContext) {
        // Create your Configuration instance, and specify if up to what FreeMarker
        // version (here 2.3.29) do you want to apply the fixes that are not 100%
        // backward-compatible. See the Configuration JavaDoc for details.

        // Specify the source where the template files come from. Here I set a
        // plain directory for it, but non-file-system sources are possible too:
        File file = new File(pathToTemplates);
        //configuration.setDirectoryForTemplateLoading(file);
        configuration.setServletContextForTemplateLoading(servletContext, "");

        // From here we will set the settings recommended for new projects. These
        // aren't the defaults for backward compatibilty.

        // Set the preferred charset template files are stored in. UTF-8 is
        // a good choice in most applications:
        configuration.setDefaultEncoding("UTF-8");

        // Sets how errors will appear.
        // During web page *development* TemplateExceptionHandler.HTML_DEBUG_HANDLER is better.
        configuration.setTemplateExceptionHandler(TemplateExceptionHandler.RETHROW_HANDLER);

        // Don't log exceptions inside FreeMarker that it will thrown at you anyway:
        configuration.setLogTemplateExceptions(false);

        // Wrap unchecked exceptions thrown during template processing into TemplateException-s:
        configuration.setWrapUncheckedExceptions(true);

        // Do not fall back to higher scopes when reading a null loop variable:
        configuration.setFallbackOnNullLoopVariable(false);
    }

    public static void preprocessConfig(Writer out, Map<String, Object> root, ServletContext context, String templateName) {
        Template template = null;
        try {
            template = FreemarkerConfig.getInstance(context.getRealPath("/WEB-INF/template"), context).getTemplate(templateName);
            template.process(root, out);
        } catch (TemplateException | IOException e) {
            e.printStackTrace();
        }
    }
}
