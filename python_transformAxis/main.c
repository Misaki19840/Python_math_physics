#include <stdio.h>

#define PI (3.14159265358979323846264338327950288)

void rotate_yaw(double* out, double* in, double theta_rad) {
    out[0] = in[0] * cos(theta_rad) - in[1] * sin(theta_rad);
    out[1] = in[0] * sin(theta_rad) + in[1] * cos(theta_rad);

//    printf("cos , %.2f \n", cos(theta_rad));
//    printf("sin , %.2f \n", sin(theta_rad));
//    printf("in[0] , %.2f \n", in[0]);
//    printf("in[1] , %.2f \n", in[1]);
}

void getlocalpos(double* out, double* in_point, double* in_t, double theta_rad) {

    double M[3][3];
    double M_T[3][3];
    M[0][0] = cos(theta_rad); M[0][1] = -sin(theta_rad); M[0][2] = 0;
    M[1][0] = sin(theta_rad); M[1][1] = cos(theta_rad); M[1][2] = 0;
    M[2][0] = 0; M[2][1] = 0; M[2][2] = 1;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            M_T[j][i] = M[i][j];
        }
    }

    printf("M =\n");
    printf("%.2f %.2f %.2f", M[0][0], M[0][1], M[0][2]);
    printf("\n");
    printf("%.2f %.2f %.2f", M[1][0], M[1][1], M[1][2]);
    printf("\n");
    printf("%.2f %.2f %.2f", M[2][0], M[2][1], M[2][2]);
    printf("\n\n");

    printf("M_T =\n");
    printf("%.2f %.2f %.2f", M_T[0][0], M_T[0][1], M_T[0][2]);
    printf("\n");
    printf("%.2f %.2f %.2f", M_T[1][0], M_T[1][1], M_T[1][2]);
    printf("\n");
    printf("%.2f %.2f %.2f", M_T[2][0], M_T[2][1], M_T[2][2]);
    printf("\n\n");

    printf("t =\n");
    printf("%.2f %.2f %.2f", in_t[0], in_t[1], in_t[2]);
    printf("\n\n");
    
    out[0] = M_T[0][0] * in_point[0] + M_T[0][1] * in_point[1] + M_T[0][2] * in_point[2] - (M_T[0][0] * in_t[0] + M_T[0][1] * in_t[1] + M_T[0][2] * in_t[2]);
    out[1] = M_T[1][0] * in_point[0] + M_T[1][1] * in_point[1] + M_T[1][2] * in_point[2] - (M_T[1][0] * in_t[0] + M_T[1][1] * in_t[1] + M_T[1][2] * in_t[2]);
    out[2] = M_T[2][0] * in_point[0] + M_T[2][1] * in_point[1] + M_T[2][2] * in_point[2] - (M_T[2][0] * in_t[0] + M_T[2][1] * in_t[1] + M_T[2][2] * in_t[2]);
}

int main()
{
    /****/
    double theta_degree = 90;

    double point_g01[3] = { -2, 3, 0 };
    double point_g02[3] = { 4, 8, 0 };
    double point_g03[3] = { 6, 3, 0 };

    double point_l01[3] = { 0, 0, 0 };
    double point_l02[3] = { 0, 0, 0 };
    double point_l03[3] = { 0, 0, 0 };

    double l_origin[3] = { 5, 5 ,0 };
    /****/


    double eg_x[3] = { 1, 0, 0};
    double eg_y[3] = { 0, 1, 0};
    double eg_z[3] = { 0, 0, 1 };
    double g_origin[3] = { 0, 0 ,0};

    double el_x[3] = { 1, 0, 0 };
    double el_y[3] = { 0, 1, 0 };
    double el_z[3] = { 0, 0, 1 };

    double t[3] = { 0, 0, 0 };
    for (int i = 0; i < 3; i++) t[i] = l_origin[i] - g_origin[i];

    double theta_rad = theta_degree * (PI / 180);

    rotate_yaw(el_x, eg_x, theta_rad);
    rotate_yaw(el_y, eg_y, theta_rad);

    getlocalpos(point_l01, point_g01, t, theta_rad);
    getlocalpos(point_l02, point_g02, t, theta_rad);
    getlocalpos(point_l03, point_g03, t, theta_rad);

    printf("point_g01 x,y,z = %.2f %.2f %.2f", point_g01[0], point_g01[1], point_g01[2]);
    printf("\n");
    printf("point_l01 x,y,z = %.2f %.2f %.2f", point_l01[0], point_l01[1], point_l01[2]);
    printf("\n\n");

    printf("point_g02 x,y,z = %.2f %.2f %.2f", point_g02[0], point_g02[1], point_g02[2]);
    printf("\n");
    printf("point_l02 x,y,z = %.2f %.2f %.2f", point_l02[0], point_l02[1], point_l02[2]);
    printf("\n\n");

    printf("point_g03 x,y,z = %.2f %.2f %.2f", point_g03[0], point_g03[1], point_g03[2]);
    printf("\n");
    printf("point_l03 x,y,z = %.2f %.2f %.2f", point_l03[0], point_l03[1], point_l03[2]);
    printf("\n\n");

//    printf("cos , %.2f \n", cos(theta_rad));
//    printf("sin , %.2f \n", sin(theta_rad));

//    printf("el_x: %.2lf  %.2lf  %.2lf \n", el_x[0], el_x[1], el_x[2]);
//    printf("el_y: %.2f  %.2f  %.2f \n", el_y[0], el_y[1], el_y[2]);

    return 0;
}