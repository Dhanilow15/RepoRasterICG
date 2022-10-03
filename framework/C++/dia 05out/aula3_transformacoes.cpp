#include <cstdlib>
#include <iostream>
#include <GL/glut.h>

void init();      
void draw();

void mouse_test(GLint button, GLint action, GLint x, GLint y);
void mouse_test2(GLint x, GLint y);
void mouse_test3(GLint x, GLint y);

void keybord_test(GLubyte key, GLint x, GLint y);
void keybord_test2(GLint key, GLint x, GLint y);

void menu_test(GLint item_number);

GLint WINDOW_WIDTH  = 500,
      WINDOW_HEIGHT = 500;

//armazena os vértices de um objeto
struct VERTEX
{
  int x;
  int y;
};
//armazena a descrição geométrica de um objeto
struct OBJECT
{
  VERTEX *vertices;
  int nrvertices;
};
OBJECT *object; //objeto global que será desenhado

OBJECT *create_object()
{
  OBJECT *obj = (OBJECT *)malloc(sizeof(OBJECT));
  obj->nrvertices = 5;
  obj->vertices = (VERTEX *)malloc(obj->nrvertices * sizeof(VERTEX));
  obj->vertices[0].x = 250;
  obj->vertices[0].y = 130;
  obj->vertices[1].x = 250;
  obj->vertices[1].y = 170;
  obj->vertices[2].x = 220;
  obj->vertices[2].y = 190;
  obj->vertices[3].x = 190;
  obj->vertices[3].y = 170;
  obj->vertices[4].x = 190;
  obj->vertices[4].y = 130;
  return obj;
}

VERTEX calculate_centroid(OBJECT *obj)
{
  int i;
  VERTEX cent;
  cent.x = 0;
  cent.y = 0;
  for (i = 0; i < obj->nrvertices; i++)
  {
    cent.x += obj->vertices[i].x;
    cent.y += obj->vertices[i].y;
  }
  cent.x /= obj->nrvertices;
  cent.y /= obj->nrvertices;
  return cent;
}
      

int main(int argc, char* argv[])
{
  glutInit(&argc, argv);
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
  
  GLint screen_width  = glutGet(GLUT_SCREEN_WIDTH),
        screen_height = glutGet(GLUT_SCREEN_HEIGHT);  
  
  glutInitWindowPosition((screen_width - WINDOW_WIDTH) / 2, (screen_height - WINDOW_WIDTH) / 2);
  glutInitWindowSize(WINDOW_WIDTH, WINDOW_WIDTH);
  glutCreateWindow("OpenGL - Transformações");
  
  init();
  glutDisplayFunc(draw);  
  glutMouseFunc(mouse_test);
  
  glutKeyboardFunc(keybord_test);
  glutSpecialFunc(keybord_test2);

  glutMainLoop();
  
  
  return EXIT_SUCCESS;
}

void init()
{
  glClearColor(1.0, 1.0, 1.0, 1.0);
  glMatrixMode(GL_PROJECTION);
  
  gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT);
  object = create_object(); //cria o objeto
}

void draw_object(OBJECT *obj)
{
  int i;
  glBegin(GL_LINE_LOOP); //desenha uma linha
  for (i = 0; i < obj->nrvertices; i++)
  {
    glVertex2i(obj->vertices[i].x, obj->vertices[i].y);
  }
  glEnd();
}

void draw()
{
  glClear(GL_COLOR_BUFFER_BIT); //desenha o fundo (limpa a janela)
  glMatrixMode(GL_MODELVIEW); //garante que a matrix seja a ModelView
  glLoadIdentity(); //carrega a matrix identidade
  
  glColor3f(0.0, 0.0, 1.0); //altera o atributo de cor
  draw_object(object); //desenha o objeto

  VERTEX cent = calculate_centroid(object); //calcula o centróide
  glColor3f(1.0, 0.0, 0.0); //altera o atributo de cor
  glTranslatef(cent.x, cent.y, 0);          //movo o centróide para a posição original
  glScalef(2, 2, 0);                        //faço a escala
  glTranslatef(-cent.x, -cent.y, 0);        //movo o centróide para a origem
  draw_object(object); //desenha o objeto
  

  glLoadIdentity();                        //carrega a matrix identidade
  glColor3f(0.0, 0.0, 0.0);                //altera o atributo de cor
  glTranslatef(cent.x, cent.y, 0);         //movo o centróide para a posição original
  glRotatef(90, 0, 0, 1);                  //rotaciono
  glTranslatef(-cent.x, -cent.y, 0);       //movo o centróide para a origem
  draw_object(object);                     //desenha o objeto
  
  glFlush();                               //processa as rotinas OpenGL o mais rápido possível
}

void mouse_test(GLint button, GLint action, GLint x, GLint y)
{
  switch(button)
  {
    case GLUT_LEFT_BUTTON: 
    {
      std::cout<<"Esquerda";
      break;
    }
    case GLUT_MIDDLE_BUTTON:
    {
      std::cout<<"Meio";
      break;
    }      
    case GLUT_RIGHT_BUTTON:
    {
      std::cout<<"Direita";
      break;
    }      
    default: break;
  }
  
  if(action == GLUT_DOWN)
    std::cout<<" preciona";
  else //GLUT_UP
    std::cout<<" libera";
  
// x cresce da esquerda pra direita. O y cresce de cima para baixo  
  std::cout<<" em (x:"<<x<<", y:"<<y<<")";
    
  std::cout<<"\n"; 
}

void mouse_test2(GLint x, GLint y)
{
  std::cout<<"Movendo mouse sem clicar para posicao (x:"<<x<<", y:"<<y<<")\n"; 
}

void mouse_test3(GLint x, GLint y)
{
  std::cout<<"Arrastando o mouse para posicao (x:"<<x<<", y:"<<y<<")\n"; 
}

void keybord_test(GLubyte key, GLint x, GLint y)
{
  GLint m = glutGetModifiers();
  
  if(m == GLUT_ACTIVE_SHIFT)
    std::cout<<"Shift ou Caps ";
  else if(m == GLUT_ACTIVE_CTRL)
    std::cout<<"Control ";
  else if(m == GLUT_ACTIVE_ALT)
    std::cout<<"Alt "; 
  
//VERIFICAR TABELA ASCII QUANDO O 'q' ou 'Q' ESTIVER PRECIONADO 
  if((GLint) key == 81 || (GLint) key == 113)
    exit(EXIT_SUCCESS);

  //ESC = 27
  if (key == 27)
    glutReshapeWindow(WINDOW_WIDTH, WINDOW_HEIGHT);
}

void keybord_test2(GLint key, GLint x, GLint y)
{
//GLUT_KEY_F1 .. GLUT_KEY_F12
//GLUT_KEY_UP, GLUT_KEY_DOWN, GLUT_KEY_LEFT, GLUT_KEY_RIGHT
//GLUT_KEY_PAGE_DOWN, GLUT_KEY_HOME etc.  
  
  std::cout<<"Tecla especial: "<<key<<" (x:"<<x<<", y:"<<y<<")\n"; 
  
  if(key == GLUT_KEY_F11)
    glutFullScreen();
}

// funcao para multiplicar duas "matrizes 4x4" (na realidade sao vetores de 16 elementos)
void multiplica(float *m1, float *m2, float *m_resultado){

    // OpenGL lida recebe vetores de 16 elementos e interpreta como matrizes 4x4.
    // Nessa funcao, transformamos as matrizes de volta para float[4][4] para facilitar a multiplicacao

    float m_a[4][4];
    float m_b[4][4];
    float m_c[4][4]; // m_c = m_a * m_b

    int n = 0;
    for(int i=0; i < 4; i++){
        for(int j=0; j < 4; j++){
            m_a[i][j] = m1[n];
            m_b[i][j] = m2[n];
            n += 1;
        }
    }


    for(int i=0;i<4;i++){    
        for(int j=0;j<4;j++){
            m_c[i][j]=0.0;
            for(int k=0; k < 4; k++){
                m_c[i][j] += m_a[i][k]*m_b[k][j];    
            }
        }
    }

    // voltando a resposta para o formato do OpenGL
    n = 0;
    for(int i=0; i < 4; i++){
        for(int j=0; j < 4; j++){
            m_resultado[n] = m_c[i][j];
            printf("%f \t",m_c[i][j]);
            n += 1;
        }
        printf("\n");
    }
    printf("-----------------------------------\n");
}


