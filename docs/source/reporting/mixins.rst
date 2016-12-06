=========
Reporting
=========
-----------------
API Documentation
-----------------
This module integrating generation model based report into pdf format
into django admin. Currently there are 2 available engine we use to generate pdf file.

   1. ReportLab using \*.rml file for layouting template.
   2. WeasyPrint using \*.html.


Utils
=====

You can use utilities in this module to generate pdf report (e.g, 
using it to make custom action in admin class)

RML2PDF
-------

.. py:class:: reporting.utils.RML2PDF(context, template_name=None, output=None)
   
   ReportLab wrapper class to generate pdf report
   with \*.rml template file

   **Attributes**

   .. autoattribute:: template_name

      html template name used to render the report

   .. autoattribute:: context

      context object used by ``render()`` function

   .. py:attribute:: RML2PDF.output

      pdf output filename, default to ``default.pdf``

   **Method**

   .. automethod:: get_template

      get template file

      :return: template

   .. automethod:: get_context_data

      get context data

      :return: context

   .. automethod:: render

      render pdf report data

      :return: HttpResponse
   
HTML2PDF
--------

.. py:class:: reporting.utils.HTML2PDF(context, template_name=None, output=None)
   
   WeasyPrint wrapper class to generate pdf report
   with \*.html template file

   **Attributes**

   .. autoattribute:: template_name

      html template name used to render the report

   .. autoattribute:: context

      context object used by ``render()`` function

   .. py:attribute:: HTML2PDF.output

      pdf output filename, default to ``default.pdf``

   **Method**

   .. automethod:: get_template

      get template file

      :return: template

   .. automethod:: get_context_data

      get context data

      :return: context

   .. automethod:: render

      render pdf report data

      :return: HttpResponse


Mixin
=====

HTMLModelReportMixin
--------------------

.. py:class:: reporting.admin.HTMLModelReportMixin

   Model mixin with WeasyPrint engine.

   Mixin for django admin to generate model object detail
   in pdf format report with WeasyPrint using html file template.

   **Attributes**   

   .. autoattribute:: report_template

      `String` path of html file template to be used for rendering the report

   .. autoattribute:: report_context_object_name

      `String`, object context used in rendered template

   .. autoattribute:: report_output   

      `String` report output file type, default to pdf format

   .. autoattribute:: change_form_template

   **Methods**

   .. automethod:: get_urls

      :return: urlpattern

   .. automethod:: get_context_data
   .. automethod:: get_report_template
   .. automethod:: get_output_filename
   .. automethod:: report


RMLModelReportMixin
-------------------
.. py:class:: reporting.admin.RMLModelReportMixin

   Model mixin with ReportLab engine.

   Mixin for django admin to generate model object detail
   in pdf format report with ReportLab \*.rml template.

   **Attributes** 

   .. autoattribute:: report_template

      `String` path of html file template to be used for rendering the report

   .. autoattribute:: report_context_object_name

      `String`, object context used in rendered template

   .. autoattribute:: report_output   

      `String` report output file type, default to pdf format

   .. autoattribute:: change_form_template

   **Methods**

   .. automethod:: get_urls

      :return: urlpattern

   .. automethod:: get_context_data
   .. automethod:: get_report_template
   .. automethod:: get_output_filename
   .. automethod:: report
