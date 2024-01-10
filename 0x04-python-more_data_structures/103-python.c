#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - this func will prt py byts
 *
 * @p: the obj for py
 *
 * Return: N/A
 */

void print_python_bytes(PyObject *p)
{

	long int x, delm, size;
	char *string;
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		delm = 10;
	else
		delm = size + 1;

	printf("  first %ld bytes:", delm);

	for (x = 0; x < delm; x++)
		if (string[x] >= 0)
			printf(" %02x", string[x]);
		else
			printf(" %02x", 256 + string[x]);

	printf("\n");
}



/**
 * print_python_list - this func willl prt
 * lst info
 *
 * @p: obj for py
 *
 * Return: N/A
 */


void print_python_list(PyObject *p)
{
	long int size, x;
	PyObject *my_object;
	PyListObject *my_lst;

	size = ((PyVarObject *)(p))->ob_size;
	my_lst = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", my_lst->allocated);

	for (x = 0; x < size; x++)
	{
		my_object = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((my_object)->ob_type)->tp_name);
		if (PyBytes_Check(my_object))
			print_python_bytes(my_object);
	}
}
