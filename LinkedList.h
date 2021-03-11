#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <algorithm>
using namespace std;

template<typename T>
class LinkedList : public LinkedListInterface<T>
{
private:
	struct Node
	{
		T data;
		Node* next;
		Node(const T& d, Node* n) : data(d), next(n) {}
		~Node() = default;
	};
	Node* head;

public:
	LinkedList() : head(NULL) {}
	~LinkedList() { clear(); }

	// Clearing the entire list
	void clear()
	{

		while (head != NULL)
		{
			Node* saved_ptr = head;
			head = saved_ptr->next;
			delete saved_ptr;
		}
		return;
	}

	// When inserting, we push the word given to the very front
	void push_front(const T& item)
	{
		Node* rand_node = new Node(item, head);
		if (head == NULL)
		{
			head = rand_node;
		}
		else
		{
			rand_node->next = head;
			head = rand_node;
		}
		return;
	}

	// insert item1 after item2
	bool insertAfter(const T& item1, const T& item2)
	{
		Node* after = find(item2);
		if (after == NULL) return false;
		after->next = new Node(item1, after->next);
		return true;
	}

	/*friend ostream& operator<<(ostream& os, LinkedList& myList)
	{
		os << myList.toString();
		return os;
	}*/

	string toString() const
	{
		stringstream out;
		Node* node_ptr = head;
		while (node_ptr != NULL)
		{
			out << node_ptr->data << " ";
			node_ptr = node_ptr->next;
		}
		return out.str();
	}

	// Deletes the first node of data
	void pop_front()
	{

		if (head != NULL)
		{
			Node* saved_ptr = head;
			head = saved_ptr->next;
			delete saved_ptr;
		}
		return;
	}

	// Displays the first node of data
	T& front()
	{
		if (head != NULL)
		{
			return head->data;
		}
		/*else
		{
			return;
		}*/
	}

	// Says if your list is empty or not
	bool empty() const
	{
		if (head == nullptr)
		{
			return true;
		}
		else
		{
			return false;
		}
	}

	// Returns size of list
	size_t size() const
	{
		int num_nodes = 0;
		Node* node_ptr = head;
		while (node_ptr != NULL)
		{
			num_nodes++;
			node_ptr = node_ptr->next;
		}
		delete node_ptr;
		return num_nodes;
	}

	// Reverses list
	void reverse()
	{
		// Initialize current, previous, next
		Node* current = head;
		Node* prev = NULL, * next = NULL;

		while (current != NULL) {
			// Store next
			next = current->next;

			// Current becomes previous
			current->next = prev;

			// Move pointers one position ahead.
			prev = current;
			current = next;
		}
		head = prev;
	}

	void remove(const T& value)
	{
		Node* prev_node = NULL;
		Node* node_str = head;
		// While the head contains something and the data in the node is not the value we seek...
		while (node_str != NULL && node_str->data != value)
		{
		
		if (node_str == NULL)
		{
			return;
		}
		// If previous node is nothing + data is found, head is the next node and we delete the data
		if (prev_node == NULL)
		{
			Node* del_node = head;
			head = head->next;
			delete del_node;
		}
		else // delete data found
		{
			prev_node->next = node_str->next;
			node_str->next = NULL;
			delete node_str;
		}
		// Move along until we find the data we seek
		prev_node = node_str;
		node_str = node_str->next;
		}
	}

	//==================================================================
	class Iterator
	{
	private:
		Node* node_;
	public:
		Iterator(Node* np) : node_(np) {}
		~Iterator() = default;
		bool operator!=(const Iterator& rhs) const { return this->node_ != rhs.node_; }
		bool operator==(const Iterator& rhs) const { return this->node_ == rhs.node_; }
		T& operator*() const { return node_->data; }
		Iterator& operator++() { if (node_ != NULL) node_ = node_->next; return *this; }

		// if you see "<<" then do the following:
		friend std::ostream& operator<< (std::ostream& os, LinkedList<T>& myList)
		{
			for (Iterator iter = myList.begin(); iter != myList.end(); ++iter)
			{
				os << *iter << " ";
			}
			return os;
		}

		// toString
		
		string to_String() const
		{
			stringstream out;
			Node* node_ptr = head;
			while (node_ptr != NULL)
			{
				out << node_ptr->data << " ";
				node_ptr = node_ptr->next;
			}
			return out.str();
		}

		//getNode function outputs the node from iterator
		Node* getNode() { return node_; }
	};


	Iterator begin() { return Iterator(this->head); }
	Iterator end() { return Iterator(NULL); }
	

	Iterator find(Iterator first, Iterator last, const T& value)
	{		
		// while we are not at the end
		while (first != last)
		{
			// if we find the value
			if (first.getNode()->data == value)
			{
				// return it
				return first;
			}
			else // else keep looking
			{
				++first;
			}
		}
		return end();
	}

	Iterator erase(Iterator position)
	{
		Node* node_ptr = position.getNode();
		Node* node_ = head;
		Node* saved_ptr = head;
		// if head is what we are trying to erase...
		if (node_ == node_ptr)
		{
			// head moves to the next link in line
			head = saved_ptr->next;
			// and we delete where it was
			delete saved_ptr;
			return begin();
		}
		while (node_ != NULL)
		{
			// if next position is what we are looking for...
			if (node_->next == node_ptr)
			{
				// we move on to the next and delete the original
				node_->next = node_ptr->next;
				delete node_ptr;
				break;
			}
			// if we are not at the position we are looking for, keep parsing
			node_ = node_->next;
		}
		return Iterator(node_);
	}

	void replace(Iterator first, Iterator last, const T& old_value, const T& new_value)
	{
		// If you iterate from the beginning to the end, and find this value x, replace with y

		while (first != last)
		{
			if (first.getNode()->data == old_value)
			{
				first.getNode()->data = new_value;
				
				//return first;
			}
			++first;
		}
	}

	Iterator insert_after(Iterator position, const T& value)
	{
		// if we are not finished looking...
		if (position != end()) {
			// new_node will be a new node that points to the next link
			Node* new_node = new Node(value, position.getNode()->next);
			position.getNode()->next = new_node;
			return Iterator(++position);
		}
	}

	//Given some spot, place value before it.

	Iterator insert(Iterator position, const T& value)
	{
		Node* node_ptr = position.getNode();
		Node* node_ = head;
		Node* old_head = head;

		if (head->data == position.getNode()->data) // if first position contains data we want...
		{
			// then we say let's make head a new node, one that points to the original head
			head = new Node(value, old_head); // puts head before the original head
			return Iterator(head);
		}

		while (node_ != NULL)
		{
			if (node_->next == node_ptr) // if next is what we are looking for...
			{
				node_->next = new Node(value, node_->next); //node_->next goes back one (insert before)
				break;
			}
			node_ = node_->next; // keep parsing through if node->next is not what we want
		}
		return Iterator(node_->next);
	}


};


#endif // LINKEDLIST_H