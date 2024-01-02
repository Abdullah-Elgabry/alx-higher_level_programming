#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - this func will insert n in S linked list
 * @head: ptr address
 * @number: the number will be insrted
 * Return: the node
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *n_nde = *head, *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!n_nde || new_node->n < n_nde->n)
	{
		new_node->next = n_nde;
		return (*head = new_node);
	}

	while (n_nde)
	{
		if (!n_nde->next || new_node->n < n_nde->next->n)
		{
			new_node->next = n_nde->next;
			n_nde->next = new_node;
			return (n_nde);
		}
		n_nde = n_nde->next;
	}
	return (NULL);
}
