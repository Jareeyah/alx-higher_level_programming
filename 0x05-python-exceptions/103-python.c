#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_float - This is a program that prints the python floats
 * @p: This is the address of the pyobject
 */
void print_python_float(PyObject *p)
{
	double f = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	f = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(f 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - This is a porgram that prints the python bytes
 * @p: This is the address of the pyobject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s = 0, b = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = PyBytes_Size(p);
	printf("  size: %zd\n", s);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", s < 10 ? s + 1 : 10);
	while (b < s + 1 && b < 10)
	{
		printf(" %02hhx", str[b]);
		b++;
	}
	printf("\n");
}

/**
 * print_python_list - A program that prints info about python lists
 * @p: This is the address of the puobject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s = 0;
	PyObject *new;
	int l = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		s = PyList_GET_SIZE(p);

		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		while (l < s)
		{
			new = PyList_GET_ITEM(p, l);
			printf("Element %d: %s\n", l, new->ob_type->tp_name);
			if (PyBytes_Check(new)
				print_python_bytes(new);
			else if (PyFloat_Check(new))
				print_python_float(new);
			l++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
