      SUBROUTINE ritout(x, n, iunit)
      IMPLICIT none
      INTEGER i, n, iunit
      REAL x(n)
      CHARACTER*90 fname
C     Reconstruction 8 Mar 2006 of vintage 1986 subroutine
C     Robert Grumbine

      WRITE(fname,9001) iunit
 9001 FORMAT("fort.",I2)
      OPEN(UNIT=iunit, FILE=fname, FORM="FORMATTED", STATUS="NEW")
      DO i = 1, n
        PRINT *,i,x(n)
      ENDDO

      RETURN
      END
CD dcheck.ross.f:        CALL ritout (n, speed, unit)
CD subsec.f:      CALL ritout (INT(nrec/del), avg, 11)
