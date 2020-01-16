#include <stdio.h>
int main(){
double grade;
double _rating;
L2: grade=12;
L3: if grade>16 goto L5;
L4: goto L8;
L5: _rating=4;
L6: TT0=_rating+1;
L7: _rating=TT0;
L8: if grade>14 goto L10;
L9: goto L11;
L10: _rating=3;goto L15;
L11: if grade>12 goto L13;
L12: goto L14;
L13: _rating=2;goto L15;
L14: _rating=1;
L15: 
print("{_rating}");
}