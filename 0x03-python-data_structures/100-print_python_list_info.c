#include <Python.h>

/**
 * print_python_list_info - C function that prints some basic info about python list
 * @p: The PyObject
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, l;
	PyObject *o;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] SIze of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (l = 0; l < size; l++)
	{
		printf("Element %d: ", l);

		o = PyList_GetItem(p, l);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
