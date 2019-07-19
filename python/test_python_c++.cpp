// https://blog.csdn.net/fitzzhang/article/details/79212411

#include <Python.h>

static PyObject *module_func(PyObject *self, PyObject *args) {
    // do ur stuff here
    Py_RETURN_NONE;
}

static PyMethodDef module_methods[] = {
    {"func", (PyCFunction)module_func, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initModule() {
    Py_InitModule3(Module, module_methods, "docstring...");
}

/*
// C func -- 模块名_函数名
static PyObject *MyFunction( PyObject *self, PyObject *args );
static PyObject *MyFunctionWithKeywords(PyObject *self,  PyObject *args, PyObject *kw);
static PyObject *MyFunctionWithNoArgs( PyObject *self );

// 方法映射表
struct PyMethodDef {
   char *ml_name;           // 暴露给python程序的函数名
   PyCFunction ml_meth;     // 函数的指针
   int ml_flags;            // METH_VARARGS | MET_KEYWORDS, METH_NOARGS
   char *ml_doc;
};
*/