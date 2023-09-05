#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_bytes - A program thatprints info about python lists
 * @p: The address of pyobject
 */
void print_python_bytes(PyObject *p)
{
	size_t b, l, size;
	char *str;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	l =  size + 1 > 10 ? 10 : size + 1;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %lu bytes: ", l);
	for (b = 0; b < l; b++)
		printf("%02hhx%s", str[b], b + 1 < l ? " " : "");
	printf("\n");
}

/**
 * print_python_list - A program that prints info about python lists
 * @p: The address of pyobject
 */
void print_python_list(PyObject *p)
{
	int l;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (l = 0; l < ((PyVarObject *)p)->ob_size; l++)
	{
		printf("Element %d: %s\n", l,
			((PyListObject *)p)->ob_item[l]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[l]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[l]);

	}
}
