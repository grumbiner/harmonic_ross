      FUNCTION yes(defalt)
C     Function to return .TRUE. if the user responds y, .FALSE. if he
C       says n, and the default value otherwise.
C     Robert Grumbine

      IMPLICIT none

      LOGICAL yes, defalt
      CHARACTER resp

      READ (11,9001) resp
      PRINT *,'resp = ',resp
 9001 FORMAT(A1)

      yes = (resp.EQ.'y') .OR. (defalt .AND. resp.NE.'y'
     1                                 .AND. resp.NE.'n')

      RETURN
      END
