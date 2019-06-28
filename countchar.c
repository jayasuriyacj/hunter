#include<stdio.h>
#include<string.h>
int main()
{
char a[100];
int b=0,c,i;
gets(a);
c=strlen(a);
for(i=0;i<c;i++)
{
if(a[i] == ' ')
{
b=b+1;
}
}
printf("%d",c-b);
return 0;
}
