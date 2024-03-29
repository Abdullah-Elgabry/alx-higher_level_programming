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
	listint_t *node = *head, *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (!node || new_node->n < node->n)
	{
		new_node->next = node;
		return (*head = new_node);
	}

	while (node)
	{
		if (!node->next || new_node->n < node->next->n)
		{
			new_node->next = node->next;
			node->next = new_node;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
