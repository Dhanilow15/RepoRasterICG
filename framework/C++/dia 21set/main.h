#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#include <iostream>

#include "definitions.h"

GLuint tex;
//background starting color
float bcgR = 0.0, bcgG = 0.0, bcgB = 0.0, bcgA = 0.0;

void (*DrawFunc)(void);

//*****************************************************************************
void house(){
    float ponto1[2], ponto2[2], ponto3[2], ponto4[2], ponto5[2], ponto6[2];
    
    ponto1[0] = 125;
    ponto1[1] = 225;
    
    ponto2[0] = 225;
    ponto2[1] = 225;

    ponto3[0] = 175;
    ponto3[1] = 175;

    ponto4[0] = 125;
    ponto4[1] = 225;

    ponto5[0] = ponto4[0] + int(COMPRIMENTO/3);
    ponto5[1] = ponto4[1] + int(ALTURA);

    ponto6[0] = 260;
    ponto6[1] = 250;

    //telhado
    glBegin(GL_TRIANGLES);
        glColor3f(0.7f, 0.5f, 0.1f);
        glVertex2f(0, 0.5);
		glColor3f(0.7f, 0.5f, 0.1f);
        glVertex2f(-0.5, -0.5);
		glColor3f(0.7f, 0.5f, 0.1f);
        glVertex2f(0.5, -0.3);
    glEnd();

	
}

void display(void)
{
	DrawFunc();

	// Copia o framebuffer para a textura.
	glBindTexture(GL_TEXTURE_2D, tex);
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, IMAGE_WIDTH, IMAGE_HEIGHT, 0, GL_RGBA, GL_UNSIGNED_BYTE, FBptr);

	glEnable(GL_TEXTURE_2D);

	// Desenha o quadrilátero com a textura mapeada
	glClearColor(bcgR, bcgG, bcgB, bcgA);
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glutPostRedisplay();

	glViewport(0, 0, IMAGE_WIDTH, IMAGE_HEIGHT);
	/**
	glBegin(GL_TRIANGLES);
		glTexCoord2f(0.0f, 1.0f);
		glVertex3f(-1.0f,-1.0f, 0.0f);
		glTexCoord2f(1.0f, 0.0f);
		glVertex3f( 1.0f, 1.0f, 0.0f);
		glTexCoord2f(0.0f, 0.0f);
		glVertex3f(-1.0f, 1.0f, 0.0f);
		glTexCoord2f(0.0f, 1.0f);
		glVertex3f(-1.0f,-1.0f, 0.0f);
		glTexCoord2f(1.0f, 1.0f);
		glVertex3f( 1.0f,-1.0f, 0.0f);
		glTexCoord2f(1.0f, 0.0f);	
		glVertex3f( 1.0f, 1.0f, 0.0f);
	glEnd();
	**/
	
	house();

	glBindTexture(GL_TEXTURE_2D, 0);
	glDisable(GL_TEXTURE_2D);

	glutSwapBuffers();
}

//*****************************************************************************
void exitprog(void)
{
	// Libera a memória referente ao framebuffer.
	if (!FBptr)
		delete [] FBptr;

	std::clog << "Exiting...\n";
}

//*****************************************************************************
void InitOpenGL(int *argc, char **argv)
{
	glutInit(argc,argv);
	glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE);
	glutInitWindowSize(IMAGE_WIDTH, IMAGE_HEIGHT);
	glutInitWindowPosition(100,100);
	glutCreateWindow("My OpenGL");
	glEnable(GL_COLOR_MATERIAL);
	
	// Ajusta a projeção ortográfica.
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glOrtho(-1.0f, 1.0f, -1.0f, 1.0f, -1.0f, 1.0f);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
}

//*****************************************************************************
void InitCallBacks(void)
{
	atexit( exitprog );
	glutDisplayFunc(display);
}

//*****************************************************************************
void InitDataStructures(void)
{
	// Aloca o framebuffer e inicializa suas posições com 0.
	FBptr = new unsigned char[IMAGE_WIDTH * IMAGE_HEIGHT * 5];
	
	for (unsigned int i = 0; i < IMAGE_WIDTH * IMAGE_HEIGHT ; i++)
	{
		FBptr[i*4]   = 0;
		FBptr[i*4+1] = 0;
		FBptr[i*4+2] = 0;
		FBptr[i*4+3] = 255;
	}

	// Cria uma textura 2D, RGBA (8 bits por componente).
	glGenTextures(1, &tex);
	glBindTexture(GL_TEXTURE_2D, tex);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
	glBindTexture(GL_TEXTURE_2D, 0);
}
