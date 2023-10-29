      SUBROUTINE velcmp(speed, dir, n)
C     Subroutine to compute u,v = speed*(cos(dir), sin(dir)) and 
C       write that out with the u and v which are on the data tape.
C     Robert Grumbine

      IMPLICIT none

C     Declare the arguments:
      INTEGER n
      REAL speed(n) 
      INTEGER dir(n)

C     Declare local variables:
      REAL radpdg
      INTEGER i
      REAL u(10000), v(10000)

      PARAMETER (radpdg = 57.29577951)

C************************************************************----------!!
      DO 1000 i = 1, n
        u(i) = speed(i) * COS( FLOAT(dir(i)) / radpdg)
        v(i) = speed(i) * SIN( FLOAT(dir(i)) / radpdg)
 1000 CONTINUE

      PRINT *,'What do you want to call the u data file?'
      CALL ritout(u, n, 12)
      CLOSE(12, STATUS='KEEP')

      PRINT *,'What do you want to call the v data file?'
      CALL ritout(v, n, 12)
      CLOSE (12, STATUS='KEEP')
      
      RETURN
      END
