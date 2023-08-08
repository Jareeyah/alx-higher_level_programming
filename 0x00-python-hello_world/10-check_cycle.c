#include "lists.h"

/**
 * check_cycle - A function in C that checks if a singly linked list
 * has a cycle in it
 * @list: This is the linked list to be checked
 * Return: 1 if there is a cycle otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *c = list;

	if (c->next != NULL)
	{
		c = c->next;
	}
	else
	{
		return (0);
	}
	while (c != list)
	{
		if (c->next == NULL)
		{
			return (0);
		}
		c = c->next;
	}
	return (1);
}
