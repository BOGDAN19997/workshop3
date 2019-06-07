CREATE OR REPLACE PACKAGE orm_create_Doc_by_Template IS


    TYPE Document_data IS RECORD(
        data_field ORM_Document.data_field%TYPE,
        percent_count INTEGER
    );


    TYPE tblDocumentdata IS TABLE OF Document_data;

    FUNCTION GetDocumentData (data_field ORM_Document.data_field%TYPE default null)
        RETURN tblDocumentdata
        PIPELINED;

END orm_create_Doc_by_Template;




CREATE OR REPLACE PACKAGE BODY orm_create_Doc_by_Template IS

    FUNCTION GetDocumentData (data_field ORM_Document.data_field%TYPE default null)
    RETURN tblDocumentdata
    PIPELINED
    IS

        TYPE Document_cursor_type IS REF CURSOR;
        Document_cursor  Document_cursor_type;

        cursor_data Document_data;
        query_str varchar2(1000);

    begin

        query_str :='select orm_create_Doc_by_Template.data_field, count(orm_create_Doc_by_Template.email)
                        from orm_create_Doc_by_Template ';

        -- optional part where
            if data_field is not null then
             query_str:= query_str||' where trim(orm_create_Doc_by_Template.data_field) = trim('''||Document_name||''') ';
            end if;
        -- end optional part

        query_str := query_str||' group by orm_create_Doc_by_Template.Document_name';



        OPEN Document_cursor FOR query_str;
        LOOP
            FETCH Document_cursor into cursor_data;
            exit when (Document_cursor %NOTFOUND);

            PIPE ROW (cursor_data);

        END LOOP;


    END GetDocumentData;

END orm_create_Doc_by_Template;

CREATE SEQUENCE orm_user_id
  MINVALUE 1
  START WITH 1
  INCREMENT BY 1;
  
CREATE OR REPLACE TRIGGER TRG_INSERT_ORM_USER
BEFORE INSERT ON ORM_USER
FOR EACH ROW
BEGIN
  :NEW.user_id:=ORM_USER_ID.NEXTVAL;
END;