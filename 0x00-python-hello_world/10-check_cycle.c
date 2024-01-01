#include <stdlib.h>
#include <stdio.h>
#include "lists.h"


/**
 * check_cycle - this func will checks if
 * a singly linked list has a cycle in it
 *
 * @list: this is a ptr that will checks
 *
 * Return: 1 if it cycle 0 if it is not
 */

int check_cycle(listint_t *list)
{
	listint_t *sl = list, *fst = list;

	while (fst && fst->next)
	{
		sl = sl->next;
		fst = fst->next->next;
		if (sl == fst)
			return (1);
	}
	return (0);
}
