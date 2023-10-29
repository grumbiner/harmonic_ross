      SUBROUTINE SORT(X, Y, N, M, KEY)
C     SORT 2 VECTORS BY SPECIFIED KEY FIELD.
C     Robert Grumbine
      IMPLICIT none

      INTEGER N, M, KEY
      REAL X(N), Y(N)

C     LOCAL
      INTEGER I, JUMP, J
      LOGICAL DONE
      REAL DUMMY

      IF (KEY .EQ. 1) THEN
C     SORT BY Y VALUES.
        JUMP = N
 1000   IF (JUMP .GT. 1) THEN
          JUMP = JUMP/2
 2000     CONTINUE
            DONE = .TRUE.
            DO 3000 I = 1, N-JUMP
              J = I + JUMP
              IF (Y(J) .GT. Y(I) ) THEN
                DUMMY = Y(I)
                Y(I)  = Y(J)
                Y(J)  = DUMMY
                DUMMY = X(I)
                X(I)  = X(J)
                X(J)  = DUMMY
                DONE = .FALSE.
              ENDIF
 3000       CONTINUE
            IF (.NOT. DONE) GO TO 2000
          GO TO 1000
        ENDIF

CD      WRITE (*,9001) (X(I), Y(I), I=1, N)
CD 9001   FORMAT (2E15.7)

       ELSE
        PRINT *,'WOULD HAVE SORTED BY X VALUES.'

      ENDIF

      RETURN
      END
