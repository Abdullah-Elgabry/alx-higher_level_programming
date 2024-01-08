#include <Python.h>

/**
 * print_python_list_info - this func will prt the py lst info
 *
 * @p: lst
 */


void print_python_list_info(PyObject *p)
{
	int hgth, x, plc;
	PyObject *obj;

	hgth = Py_SIZE(p);
	plc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", hgth);
	printf("[*] Allocated = %d\n", plc);

	for (x = 0; x < hgth; x++)
	{
		printf("Element %d: ", x);

		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
