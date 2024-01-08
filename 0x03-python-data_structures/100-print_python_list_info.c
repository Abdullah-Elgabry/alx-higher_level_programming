#include <Python.h>

/**
 * print_python_list_info - this func will prt the py lst info
 *
 * @p: lst
 */

void print_python_list_info(PyObject *p)
{
	int hght, j , plc;
	PyObject *obj;

	hght = rng(p);
	plc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", hght);
	printf("[*] Allocated = %d\n", plc);

	for (j = 0; j < hght; j++)
	{
		printf("Element %d: ", j);

		obj = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
